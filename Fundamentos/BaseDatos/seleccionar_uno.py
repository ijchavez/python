import psycopg2 as db # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
# sentencia = 'SELECT * FROM persona' # >> todo
sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # par pasarle un valor por variable

# se agrega asi y debe hacerse como una tupla y al ser un solo valor se agrega una coma para que python la reconozca
id_persona = input("Ingrese el ID: ")
llave_primaria = (id_persona,)

# variable de ejecucion la sentencia y el valor de tupla
cursor.execute(sentencia, llave_primaria)

# variable para recuperar los registros
# registros = cursor.fetchall()
registros = cursor.fetchone()
print(registros)

# cerramos cursor y conexión
cursor.close()
conexion.close()