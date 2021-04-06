from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO(Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s , email = %s where id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR)) # manda a imprimir el query q se va a ejecutar pero en la base de datos
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0],registro[1],registro[2],registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            # necesito obtener el conexion para guardar en la BD
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR)) # manda a imprimir el query q se va a ejecutar pero en la base de datos
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email()) #valores a insertar
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        
        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al insertar una persona :{e}')

        
        finally:
            Conexion.cerrar()
    

    @classmethod
    def actualizar(cls, persona):
        try:
            # necesito obtener el conexion para guardar en la BD
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR)) # manda a imprimir el query q se va a ejecutar pero en la base de datos
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id_persona()) #valores a insertar
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        
        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al actualizar una persona :{e}')

        
        finally:
            Conexion.cerrar()
    
    @classmethod
    def eliminar(cls, persona):
        try:
            # necesito obtener el conexion para guardar en la BD
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR)) # manda a imprimir el query q se va a ejecutar pero en la base de datos
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(), ) #valores a insertar
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        
        except Exception as e:
            conexion.rollback()
            logger.error(f'Error al insertar una persona :{e}')

        
        finally:
            Conexion.cerrar()

# if __name__ == "__main__":
    # probar el select
    # personas = PersonaDao.seleccionar()
    # for persona in personas:
    #     logger.debug(persona)
    #    logger.debug(persona.get_id_persona())
    
    # Insertar el registro
    # persona = Persona(nombre ='Pedro', apellido='Najera', email='pnajera@mail.com')
    # personas_insertadas = PersonaDao.insertar(persona)
    # logger.debug(f'Registros Insertados: {personas_insertadas}')
    
    # Actualizar registros
    # persona = Persona(id_persona = 1, nombre ='Juan', apellido='Perez', email='jperez@mail.com')
    # personas_modificadas = PersonaDao.actualizar(persona)
    # logger.debug(f'Registros actualizados: {personas_modificadas}')

    # Eliminar registro    
    # persona = Persona(id_persona = 20)
    # personas_eliminadas = PersonaDao.eliminar(persona)
    # logger.debug(f'Registros Eliminados: {personas_eliminadas}')