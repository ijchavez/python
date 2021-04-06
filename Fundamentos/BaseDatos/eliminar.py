import psycopg2 as db # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
sentencia = 'DELETE FROM persona WHERE id_persona = %s ' # modificar o actualizar
entrada = input("inserte un valor id valido a eliminar: ")
valores = (entrada,)

cursor.execute(sentencia, valores)

# guardamos la informacion en la BD
conexion.commit()

# recuperamos la cantidad de registros insertados
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

# cerramos cursor y conexión
cursor.close()
conexion.close()