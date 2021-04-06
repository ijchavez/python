from usuario import Usuario
from logger_base import logger
from cursor_del_pool import CursorDelPool

class UsuarioDao:
    '''
    DAO(Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad Usuarios
    '''
    __SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:  
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)   
            return usuarios   
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password(), usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
       
            
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount   

# if __name__ == "__main__":
    # probar el select
    # usuarios = UsuarioDao.seleccionar()
    # for usuario in usuarioss:
    #     logger.debug(usuarios)
    #     logger.debug(usuario.get_id_usuario())

    # Insertar el registro
    #  usuario = usuario(nombre ='Pedro', apellido='Najera', email='pnajera@mail.com')
    #  usuarios_insertadas = UsuarioDao.insertar(usuario)
    #  logger.debug(f'Registros Insertados: {usuarios_insertadas}')

    # Actualizar registros
    #  usuario = usuario(id_usuario = 21, nombre ='Bart', apellido='Simpson', email='bsimpson@springfield.com')
    #  usuarios_modificadas = UsuarioDao.actualizar(usuario)
    #  logger.debug(f'Registros actualizados: {usuarios_modificadas}')

    # Eliminar registro
    # usuario = usuario(id_usuario = 21)
    # usuarios_eliminadas = UsuarioDao.eliminar(usuario)
    # logger.debug(f'Registros Eliminados: {usuarios_eliminadas}')