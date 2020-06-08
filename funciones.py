# Se define
def my_funcion():
  print("Hello World!")

# Se invoca/Se llama
my_funcion()

def crear_producto(nombre_del_producto, precio):
  prod = {
    "nombre": str(nombre_del_producto),
    "precio": int(precio)
  }

  return prod

mi_producto = crear_producto("BigMac", 150)

print(mi_producto)
