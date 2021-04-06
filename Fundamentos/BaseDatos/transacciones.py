import psycopg2 as db # al hacer esto no hay q escribir mas psycopg2

conexion = db.connect(user='postgres',
                            password='postgres',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

try:
    # conexion.autocommit = True # en caso de no usar el conexion.commit()
    # variable para el cursor
    cursor = conexion.cursor()
    # variable de sentencia
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)' # par pasarle un valor por variable
    valores = ('Carl','Carlson','ccarlson@springfield.com')

    cursor.execute(sentencia, valores)

    sentencia1 = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s' # modificar o actualizar
    valores1 = ('Fabiana','Petersen','fpetersen@mail.com', 1)

    cursor.execute(sentencia1, valores1)

    # guardamos la informacion en la BD
    conexion.commit() # se saca al usarse el autocommit

except Exception as e:
    #rollback marcha atras
    conexion.rollback()
    print(f'Ocurrió un error en la transacción : {e}')

finally:
    # cerramos cursor y conexión
    cursor.close()
    conexion.close()