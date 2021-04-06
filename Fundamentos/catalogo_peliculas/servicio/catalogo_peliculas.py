import os # para eliminar archivos

class CatalogoPeliculas:
    
    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            # a es el modo append
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")
            print(pelicula.__str__() + " Agregado exitosamente") 
            
        except Exception as e:
            print("Ocurrio una excepción al agregar:", e)
        
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catálogo de Películas:")
            print(archivo.read()) 
        except Exception as e:
            print("Ocurrió un error al listar películas: ", e)
        finally:
            archivo.close()     

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo eliminado:", CatalogoPeliculas.ruta_archivo)

        except Exception as e:
            print("Ocurrio un error al eliminar", e)
