import psycopg2 as db # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s' # modificar o actualizar
valores = ('Juan1','Perez2','jperez3@mail.com', 1)

cursor.execute(sentencia, valores)

# guardamos la informacion en la BD
conexion.commit()

# recuperamos la cantidad de registros insertados
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

# cerramos cursor y conexión
cursor.close()
conexion.close()