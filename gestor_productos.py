productos = []

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
    except FileNotFoundError:
        print("No se encontró el archivo de productos. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

def añadir_producto():
    nombre = input("Por favor, ingrese el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto: ").replace('.', ''))
        cantidad = int(input("Introduce la cantidad del producto: "))
        productos.append({
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        })
        print(f"Producto '{nombre}' añadido con éxito.")
    except ValueError:
        print("Error: Introduce un número válido para el precio y la cantidad.")

def ver_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        print("Productos disponibles:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ").strip().lower()  # Convertir a minúsculas y quitar espacios
    for producto in productos:
        if producto['nombre'].lower() == nombre:  # Comparar en minúsculas
            nuevo_nombre = input("Introduce el nuevo nombre (dejar en blanco para no cambiar): ").strip()
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            nuevo_precio = input("Introduce el nuevo precio (dejar en blanco para no cambiar): ").strip()
            if nuevo_precio:
                producto['precio'] = float(nuevo_precio)
            
            nueva_cantidad = input("Introduce la nueva cantidad (dejar en blanco para no cambiar): ").strip()
            if nueva_cantidad:
                producto['cantidad'] = int(nueva_cantidad)
            
            print("Producto actualizado con éxito.")
            
            # Guardar los cambios en el archivo
            guardar_datos()
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ").strip().lower()  # Convertir a minúsculas y quitar espacios
    for producto in productos:
        if producto['nombre'].lower() == nombre:  # Comparar en minúsculas
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            
            # Guardar los cambios en el archivo
            guardar_datos()
            return
    print("Producto no encontrado.")


def menu():
    cargar_datos()  # Cargar datos al iniciar el programa
    while True:
        print("\nMenú:")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
