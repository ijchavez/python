print("Proporcione los siguientes datos del libro:")
nombre = input("Ingrese el nombre: ")
id = int(input("Ingrese el ID: "))
precio = float(input("ingrese precio: "))
envioGratuito = input("indica si el envio es gratuito(True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"
    
print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)
print("Envío Gratuido?:", envioGratuito)

print("la variable envioGratuito es:", type(envioGratuito))
