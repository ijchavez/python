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
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # par pasarle varios valores

# se agrega asi y debe hacerse como una tupla y al ser un solo valor se agrega una coma para que python la reconozca
# id_persona = input("Ingrese el ID: ")
entrada = input("proporciona las pk a buscar separado por comas: ")
tupla = tuple(entrada.split(',')) # convertir elementos que, separados por comas se hagan tupla
llaves_primarias = (tupla,) # necesario para que sea tupla de tuplas
# variable de ejecucion la sentencia y el valor de tupla
cursor.execute(sentencia, llaves_primarias)
# uno debajo del otro
registros = cursor.fetchall()
for registo in registros:
    print(registo)
# variable para recuperar los registros

print(registros)

# cerramos cursor y conexión
cursor.close()
conexion.close()