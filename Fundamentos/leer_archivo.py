try:
    archivo = open("prueba.txt", "r")
    # print(archivo.read())
    # print(archivo.read(5)) # cantidad de caracteres especifica
    # print(archivo.read(3)) # despues de los 5 otros 3
    # print(archivo.readline()) # una linea

    # iterar
    #for linea in archivo:
    #    print(linea)

    # leer todas las lineas
    # print(archivo.readlines())

    # leer una linea en particular
    # print(archivo.readlines()[1])
    
    #abrimos un nuevo archivo
    archivo2 = open("copia.txt", "w") # borrar y escribir por la w
    #archivo2 = open("copia.txt", "a") # anexar informacion 
    #copiar info del archivo 1 al 2
    archivo2.write(archivo.read())
    

except Exception as e:
    print(e)

finally:
    archivo.close() # para asegurarnos que siempre se cierre
    archivo2.close()