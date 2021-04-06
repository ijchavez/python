from logger_base import logger
class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None): #None para omitir el envio de argumentos y que el que es automatico no chille
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
        
    
    #SET/GET ID_PERSONA
    def get_id_usuario(self):
            return self.__id_usuario
        
    def set_id_persona(self, id_usuario):
        self.self.__id_usuario = id_usuario
    
    #SET/GET NOMBRE
    def get_username(self):
            return self.__username
        
    def set_username(self, username):
        self.__username = username

    #SET/GET APELLIDO
    def get_password(self):
            return self.__password
        
    def set_password(self, password):
        self.__password = password

    def __str__(self):
        cadena = (
            f'ID Persona: {self.__id_usuario}, '
            f'Nombre: {self.__username}, '
            f'Apellido: {self.__password}, '
            
        )
        return cadena


# if __name__ == '__main__':
    # usuario1 = Usuario(3,'ibanez','1234')
    # logger.debug(usuario1)
    
    #simulando un objeto a insertar de tipo persona
    # usuario2 = Usuario(4,'gchavez','11234')
    # logger.debug(usuario2)

    # usuario3 = Usuario(username="flopez", password='6958')
    # logger.debug(usuario3)
    
    #Simular el caso a eliminar un objeto de tipo persona
    # usuario4 = Usuario(id_usuario=4)
    # logger.debug(usuario4)
    