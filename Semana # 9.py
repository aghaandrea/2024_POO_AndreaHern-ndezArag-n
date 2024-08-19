class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if not any(p.obtener_id() == producto.obtener_id() for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido exitosamente.")
        else:
            print("Error: El ID del producto ya existe.")

    def eliminar_producto(self, id):
        productos_antes = len(self.productos)
        self.productos = [p for p in self.productos if p.obtener_id() != id]
        if len(self.productos) < productos_antes:
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.obtener_id() == id:
                if cantidad is not None:
                    producto.establecer_cantidad(cantidad)
                if precio is not None:
                    producto.establecer_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.obtener_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("Inventario de productos:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventarios ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: La cantidad debe ser un número entero y el precio debe ser un número decimal.")

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    menu()