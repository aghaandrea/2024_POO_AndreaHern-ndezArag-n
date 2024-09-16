import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):

        # Configuración de la ventana principal
        self.root = root
        self.root.title(
            self.root = root
        self.root.t

        self.root = root

        self

        "Aplicación GUI Básica")



        # Etiqueta
        self.label = tk.Label(root, text=
        self.label = tk.Label(roo

        self.label = tk

        self.labe

        "Ingrese un ítem:")
        self.label.pack(pady=
                        self.label.pack(pady=

                                        self.label.pa

        self

        5)







        # Campo de texto
        self.entry = tk.Entry(root, width=
        self.entry = tk.Entry(root,

                              self.entry = tk.Entry(r

        self.entry = tk.E

        self

        40)
        self.entry.pack(pady=
                        self.entry.pack(pad

        se

        5)




        # Botón "Agregar"
        self.boton_agregar = tk.Button(root, text=
        self.boton_agregar = tk.Button

        self.boton_agregar = t

        self.b
        "Agregar", command = self.agregar_item)
        self.boton_agregar.pack(pady=
                                self.boton_agregar.pack(pady=

                                                        self.boton_agreg

        self.boto

        5)




        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(root, text=
        self.boton_limpiar = tk.Button(ro

        self.boton_limpiar

        sel

        "Limpiar", command = self.limpiar_datos)
        self.boton_limpiar.pack(pady=
                                self.boton_limpiar.pack

        self.bo

        sel

        5)




        # Lista para mostrar datos
        self.lista = tk.Listbox(root, width=
        self.lista = tk.Listbox(

            self.lista = tk.L

        se

        50, height = 10)
        self.lista.pack(pady=
        self.lista.pack(

            10)

    def agregar_item(self):

        # Obtener el texto del campo de texto
        item = self.entry.get()

        item = self.entry.get(

            item=se

        i

        if item:
        # Añadir el ítem a la lista
            self.lista.insert(tk.END, item)

        self.lista.insert(tk.END, item)

        self.lista.insert(tk.END, it

        self.lista.insert(

            self.li

        # Limpiar el campo de texto
        self.entry.delete(
            self.en

        0, tk.END)

        e
        else:


        # Mostrar un mensaje de advertencia si el campo está vacío
        messagebox.showwarning(
            messagebox.showwarn

        messagebox.sh

        "Advertencia", "El campo de texto está vacío")

        def limpiar_datos(self):

            # Limpiar la lista y el campo de texto
            self.lista.delete(
                self.lista.dele

            self

            0, tk.END)
            self.entry.delete(
                self.entry.delete(

                    self.entry.dele

            self.en

            sel

            0, tk.END)

            if __name__ == "__main__":
            # Crear la ventana principal
                root = tk.Tk()
            app = AplicacionGUI(root)

            root = tk.Tk()
            app = AplicacionGUI(root)

            root = tk.Tk()
            app = Aplicacion

            root = tk.Tk()

            root

            ro

            # Iniciar el bucle principal de la aplicación
            root.mainloop()

            root.m