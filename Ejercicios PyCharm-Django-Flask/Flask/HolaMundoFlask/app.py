from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'


# niveles de manejo de logging
#
# app.logger.debug('Valor para debuguear')
# app.logger.warning('Manejo de warnings {½d variable}', 42)
# app.logger.error('Ocurrió un error')
#

rutaInicio = '/'
@app.route(rutaInicio)
def inicio():
    username = "username"
    mensajenologin = 'No ha hecho login'
    if username in session:
        return f'El usuario ya ha hecho login {session[username]}'
    return mensajenologin


rutaLogin = '/login'
@app.route(rutaLogin, methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # omitimos validacion de usuario y pass
        # En los corchetes debe usarse el nombre indicado en el for del label:
        #<label for="username">Usuario</label>
        usuario = request.form['username']
        #agregamos el usuario a la sesion:
        session['username'] = usuario
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


# pasamos un string como variable
rutaSaludar = '/saludar/<nombre>'
@app.route(rutaSaludar)
def saludar(nombre):
    cadena = f'Saludos {nombre}'
    return cadena


# pasamos un int como variable
rutaEdad = '/edad/<int:edad>'
@app.route(rutaEdad)
def mostrar_edad(edad):
    cadena = f'Tu edad es de {edad}'
    return cadena


rutaMostrarNombre = '/mostrar/<nombre>'
@app.route(rutaMostrarNombre, methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    # return render_template('archivo.html', llave=valor)
    template = 'mostrar.html'
    return render_template(template, nombre=nombre)


#REDIRECCIONAR
@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))


#MANEJO DE ERRORES
@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

#REST Representational State Transfer
#API Application Program Interface
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)