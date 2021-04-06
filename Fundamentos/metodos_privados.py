class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        """Sin guion bajo, atributo publico"""
        self.nombre = nombre
        """1 guion bajo, atributo protected"""
        self._ape_paterno = ape_paterno
        """2 guiones bajo, atributo privado"""
        self.__ape_materno = ape_materno
    
    """El GET tiene Return y solo llama el self"""
    def get_ape_materno(self):
        return self.__ape_materno
    
    """El SET no tiene Return y llama el self y la variable del metodo"""    
    def set_ape_materno(self, ape_materno):
        self.__ape_materno = ape_materno
        
    def get_ape_paterno(self):
        return self._ape_paterno
        
    def set_ape_paterno(self, ape_paterno):
        self._ape_paterno = ape_paterno    
            
    """Llamamos a un metodo publico para llamar al metodo privado"""    
    def metodo_publico(self):
        self.__metodo_privado()
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_paterno)
        print(self.__ape_materno)
        
p1 = Persona("Juan", "Lopez", "Perez")
# p1.__metodo_privado() no se puede acceder debido a que es privado
p1.metodo_publico()

print(p1.nombre)
print(p1._ape_paterno) # <<< Evitar acceder directamente al atributo
#print(p1.__apellido_materno) # <<< no permite acceder debido a que es privado, hacer metodo get y set
print("Con funcion get() atr privado:",p1.get_ape_materno())
print("Con funcion get() atr protected:",p1.get_ape_paterno())