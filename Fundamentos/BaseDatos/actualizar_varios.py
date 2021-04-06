import psycopg2 as db  # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                      password='postgres',
                      host='127.0.0.1',
                      port='5432',
                      database='test_db')

# variable para el cursor
cursor = conexion.cursor()
# variable de sentencia
# modificar o actualizar
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 1),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 2)

)

cursor.executemany(sentencia, valores)

# guardamos la informacion en la BD
conexion.commit()

# recuperamos la cantidad de registros insertados
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

# cerramos cursor y conexión
cursor.close()
conexion.close()
