import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
sentencia = 'SELECT * FROM persona'

# variable de ejecucion
cursor.execute(sentencia)

# variable para recuperar los registros
registros = cursor.fetchall()
print(registros)

# cerramos cursor y conexión
cursor.close()
conexion.close()
