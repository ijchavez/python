from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import PersonaForm
from models import Persona

app = Flask(__name__)

# INTEGRACION CON SQLALCHEMY
# Configuración DB
USER_DB = 'postgres'
PASS_DB = 'postgres'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

# SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
# esto lo comento porque se pasa a la clase database.py
# db = SQLAlchemy(app)
db.init_app(app)

# Flask Migrate
migrate = Migrate()
migrate.init_app(app, db)

# Flask WTF
app.config['SECRET_KEY']='llava_secreta'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    app.logger.debug(f'Listado de Personas: {personas}')
    app.logger.debug(f'Cantidad de Personas: {total_personas}')
    return render_template('index.html', personas=personas, total_personas=total_personas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    # Recuperamos la persona segun el ID proporcionado
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    # Instanciamos la clase de modelo
    # Instanciamos la clase form y le asociamos la clase de modelo
    # Mostramos formulario
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar {persona}')
            # insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma=personaForm)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # Recuperamos el objeto persona a editar de la base de datos
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a actualizar: {persona}')
            # no es necesario el add ya que la db esta abierta en este punto
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma=personaForm)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    # Recuperamos el objeto persona a editar de la base de datos
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))