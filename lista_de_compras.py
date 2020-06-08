lista_de_compras = []
preguntar_de_vuelta = True

while preguntar_de_vuelta:
  # obtiene el producto del usuario
  item = input("Ingrese producto: ")
  # agrega el producto a la lista
  lista_de_compras.append(item)
  # preguntar si desea continuar
  continuar = int(input("Desea agregar otro item?: (0: No/1: Si)"))

  if continuar == 1:
    continue
  else:
    preguntar_de_vuelta = False
    break

print("Seleccion de la lista: ")

for producto in lista_de_compras:
    print(producto)

