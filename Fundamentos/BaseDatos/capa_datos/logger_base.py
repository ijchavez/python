# Crear la conexion
# el cursor y el cierre de la conexion.

import logging

logger = logging
# establecemos el nivel que queremos mostrar el mensaje
logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s: [%(filename)s: %(lineno)s] %(message)s',
                   datefmt='%Y-%m-%d %I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])

if __name__ == '__main__':
    logger.warning('mensaje a nivel warning')
    logger.info('mensaje a nivel info')
    logger.debug('mensaje a nivel debug')  # resolver un problema
    logger.error('Error de BD')
