# Aplicacion de Maquina Registradora
# int = Integer (EN) -> Numero Entero (ES)
# str = String (EN) -> Cadena de Caracteres (ES) Textos o Letras

def caja_registradora():
  lista_de_productos = obtener_lista_de_productos()
  mostrar_resumen(lista_de_productos)

def crear_producto(nombre_del_producto, precio):
  prod = {
    "nombre": str(nombre_del_producto),
    "precio": int(precio)
  }

  return prod

def obtener_lista_de_productos():
  lista_de_productos = []
  preguntar_de_vuelta = True

  while preguntar_de_vuelta:
    # obtiene el nombre del producto del usuario
    nombre_del_producto = input("Ingrese producto: ")
    precio_del_producto = input("Ingrese precio del producto: ")

    # se crea un producto
    prod = crear_producto(nombre_del_producto, precio_del_producto)

    # agrega el producto a la lista
    lista_de_productos.append(prod)

    # preguntar si desea continuar
    continuar = int(input("Desea agregar otro item?: (0: No/1: Si)"))

    if continuar == 1:
      continue
    else:
      preguntar_de_vuelta = False
      break

  return lista_de_productos

def mostrar_resumen(lista_de_prod):
  print("-----------------------------")
  total = 0

  for prod in lista_de_prod:
    print(prod["nombre"] + " Precio: " + str(prod["precio"]))
    total = total + prod["precio"]

  print("-----------------------------")
  print("Total a Pagar: " + str(total))

caja_registradora()
