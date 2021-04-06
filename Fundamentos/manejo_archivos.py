try:
    archivo = open("prueba.txt","w")
    archivo.write("agregar info al archivo" + "\n")
    archivo.write("adios")
except Exception as e:
    print(e)

finally:
    archivo.close() # para asegurarnos que siempre se cierre