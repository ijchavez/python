from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    # inicio de sintaxis de with
    def __enter__(self):
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        logger.debug(f'Inicio del with método __enter__: {self.__conn}')
        return self.__cursor
    
    # Fin del bloque with
    def __exit__(self, exc_type, exc_value, exc_traceback):
        logger.debug(f'Se ejecuta el método __exit__()')
        if exc_value is not None:
            self.__conn.rollback()
            logger.debug(f'Ocurrió una exepción {exc_value}')
        
        else:

            self.__conn.commit()
            logger.debug(f'Commit de la transacción')
        # Cerramos el cursor en cualquiera de los casos
        self.__cursor.close()
        # Regresar la conexión al pool
        Conexion.liberarConexion(self.__conn)
        
if __name__ == '__main__':
    # Obtenemos un cursor a partir de la conexion del pool
    # Se ejecuta primero el metodo enter y termina con exit
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de personas')
        logger.debug(cursor.fetchall())