# Clase Archivo que utiliza constructores y destructores
class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Se llama automáticamente cuando se crea una instancia de la clase.

        Argumentos:
        nombre (str): El nombre del archivo a abrir.
        """
        self.nombre = nombre
        self.archivo = open(self.nombre, "w")
        print(f"Archivo '{self.nombre}' abierto.")

    def escribir(self, contenido):
        """
        Método para escribir en el archivo.

        Argumentos:
        contenido (str): El contenido a escribir en el archivo.
        """
        self.archivo.write(contenido)
        print(f"Se ha escrito en el archivo '{self.nombre}':\n{contenido}")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se llama automáticamente cuando se elimina una instancia de la clase.
        Cierra el archivo correctamente.
        """
        if hasattr(self, 'archivo') and self.archivo is not None:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un archivo y escribir en él
    archivo1 = Archivo("mi_archivo.txt")
    archivo1.escribir("Primera línea.\nSegunda línea.\n")

    # Al salir del bloque, se llamará automáticamente al destructor (__del__)