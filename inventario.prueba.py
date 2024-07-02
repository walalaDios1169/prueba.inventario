inventario = {}

#funcion para agregar producto
def agregar_producto():
  ID = input("ingrese el ID del producto: ")
  nombre = input("ingrese el Nombre del producto: ")
  cantidad = int(input("ingrese la cantidad del producto: "))
  precio = float(input("ingrese el precio del producto: "))
  inventario[ID] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio} 
  print("producto agregado")

#funcion para eliminar producto
def eliminar_producto():
  ID = input("ingrese el ID del producto que decea eliminar: ")
  if ID in inventario:
    del inventario[ID]
    print("producto eliminado")
  else:
    print("El producto no existe en el inventario.")

#funcion para buscar producto por su id
def buscar_producto():
  ID = input("ingrese el ID del producto que esta buscando: ")
  if ID in inventario:
    producto = inventario[ID]
    print("resultado")
    print("ID:", ID)
    print("Nombre:", producto['nombre'])
    print("Cantidad:", producto['cantidad'])
    print("Precio:", producto['precio'])
  else:
    print("El producto no se encuentra en el inventario.")

#funcion para mostrar el inventario 
def listar_inventario():
  if inventario:
    print("Inventario:")
    for ID, producto in inventario.items():
      print(f"ID: {ID}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
  else:
    print("El inventario está vacío.")

#guardar inventario en archivo
def guardar_inventario():
  with open('inventario.txt', mode='a') as inventario_csv:
    for ID, producto in inventario:
      inventario_csv.write(f"{ID}, {producto['nombre']}, {producto['cantidad']}, {producto['precio']}")

#cargar archivo guardado
def cargar_inventario():
  with open('inventario.txt', mode='r', newline="") as inventario_csv:
    for i in inventario_csv():
      print(i)
    

#menu
while True:
  print("1. agregar producto: ")
  print("2. eliminar producto: ")
  print("3. buscar producto: ")
  print("4. listar inventario:")
  print("5. salir: ")


  try:
    opcion = int(input("ingrese una opcion: "))
  except ValueError:
    print("opcion no valida")
    continue 

  if opcion == 1:
    agregar_producto()


  elif opcion == 2:
    eliminar_producto()


  elif opcion == 3:
    buscar_producto()


  elif opcion == 4:
    listar_inventario()

#salir
  elif opcion == 5:
    print("hasta luego!")
    break 
  else:
    print("Opción inválida. Por favor, ingrese un número del 1 al 5.")