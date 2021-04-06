from logger_base import logger
import psycopg2 as db  # al hacer esto no hay q escribir mas psycopg2
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'postgres'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Conexion Exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la Base de datos: {e}')
                sys.exit()
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrió el cursor con exito: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener un cursor: {e}')
                sys.exit()
        
        else:
            return cls.__cursor


    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            
            except Exception as e:
                logger.error(f'Error al cerrar cursor : {e}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            
            except Exception as e:
                logger.error(f'Error al cerrar conexión : {e}')
        logger.debug('Se han cerrado los objetos de conexión y cursor')
    
if __name__ == '__main__':
    #logger.info(Conexion.obtenerConexion())
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()