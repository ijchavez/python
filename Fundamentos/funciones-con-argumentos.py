nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese una edad: "))

def funcion_arg(nombre, edad):
    print("El nombre recibido es:",nombre, "de", edad,"años")

funcion_arg(nombre, edad)

def funcion_arg(nombre, apellido):
    print("El nombre recibido es:",nombre)
    print("El apellido recibido es:",apellido)

funcion_arg("Gerardo","Chavez")
