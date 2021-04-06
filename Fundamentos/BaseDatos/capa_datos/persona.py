from logger_base import logger
class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None): #None para omitir el envio de argumentos y que el que es automatico no chille
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
    
    #SET/GET ID_PERSONA
    def get_id_persona(self):
            return self.__id_persona
        
    def set_id_persona(self, id_persona):
        self.self.__id_persona = id_persona
    
    #SET/GET NOMBRE
    def get_nombre(self):
            return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

    #SET/GET APELLIDO
    def get_apellido(self):
            return self.__apellido
        
    def set_apellido(self, apellido):
        self.__nombre = apellido

    #SET/GET EMAIL
    def get_email(self):
            return self.__email
        
    def set_email(self, email):
        self.__nombre = email

    def __str__(self):
        cadena = (
            f'ID Persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__email}'
        
        )
        return cadena


if __name__ == '__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@mail.com')
    logger.debug(persona1)
    
    #simulando un objeto a insertar de tipo persona
    persona2 = Persona(None,'Juan','Perez','jperez@mail.com')
    logger.debug(persona2)

    persona3 = Persona(nombre="Karla", apellido='Gomez', email='kgomez@mail.com')
    logger.debug(persona3)
    
    #Simular el caso a eliminar un objeto de tipo persona
    persona4 = Persona(id_persona=4)
    logger.debug(persona4)
    