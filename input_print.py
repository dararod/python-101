# input/output

nombre = ""
apellido = ""
edad = 0
es_mayor_de_edad = None

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese edad: "))

if edad > 18:
  es_mayor_de_edad = True
else:
  es_mayor_de_edad = False

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Edad: " + str(edad))
print("Es Mayor de Edad: " + str(es_mayor_de_edad))
