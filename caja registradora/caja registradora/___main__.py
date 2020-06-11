class Producto:
  def __init__(self, id, descripcion, precio, stock):
    self.id = id
    self.descripcion = descripcion
    self.precio = precio
    self.stock = stock
  def print(self):
    print(self.id,
      self.descripcion,
      self.stock,
      self.fmt_precio())
  def fmt_precio(self):
    return str(self.precio) + " Bs"
  def precio_total(self):
    return self.precio * self.stock
# leer el archivo "inventario.csv" y devolver
# su contenido como string
def leer_inventario():
  file = open("./inventario.csv", "r")
  return file.read()
# leer cada linea y convertirla en lista de
# lineas
def convertir_en_lineas(contenido_de_inventario):
  return contenido_de_inventario.split("\n")
# convertir linea en producto
def hacer_producto_desde_linea(linea):
  datos_de_la_linea = linea.split(",")
  nuevo_producto = Producto(datos_de_la_linea[0],
    datos_de_la_linea[1],
    datos_de_la_linea[2],
    datos_de_la_linea[3])
  return nuevo_producto
contenido = leer_inventario()
print("CONTENIDO")
print(contenido)
lineas = convertir_en_lineas(contenido)
print("LINEAS")
print(lineas)