import psycopg2 as db # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)' # par pasarle un valor por variable
valores = ('Carlos','Lara','clara@mail.com')

cursor.execute(sentencia, valores)

# guardamos la informacion en la BD
conexion.commit()

# recuperamos la cantidad de registros insertados
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

# cerramos cursor y conexión
cursor.close()
conexion.close()