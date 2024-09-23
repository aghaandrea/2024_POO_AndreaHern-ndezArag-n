import tkinter as tk
from tkinter import ttk
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")

        # Frame para la lista de eventos
        self.event_frame = ttk.Frame(root)
        self.event_frame.pack(side="top", fill="both", expand=True)

        # Treeview para mostrar los eventos
        self.event_tree = ttk.Treeview(self.event_frame, columns=("fecha", "hora", "descripcion"))
        self.event_tree.heading("fecha", text="Fecha")
        self.event_tree.heading("hora", text="Hora")
        self.event_tree.heading("descripcion", text="Descripción")
        self.event_tree.pack(side="left", fill="both", expand=True)

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(self.event_frame, orient="vertical", command=self.event_tree.yview)
        self.event_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Frame para los campos de entrada y botones
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(side="bottom")

        # Campos de entrada
        self.date_entry = ttk.Entry(self.input_frame)
        self.time_entry = ttk.Entry(self.input_frame)
        self.description_entry = ttk.Entry(self.input_frame)

        # Botones
        self.add_button = ttk.Button(self.input_frame, text="Agregar Evento", command=self.add_event)
        self.delete_button = ttk.Button(self.input_frame, text="Eliminar Evento", command=self.delete_event)

        # ... (colocar los widgets en el frame y configurar los eventos)

    def add_event(self):
        # Obtener datos de los campos de entrada
        # Agregar el evento a la lista o diccionario
        # Actualizar el Treeview
        pass

    def delete_event(self):
        # Obtener el evento seleccionado en el Treeview
        # Eliminar el evento de la lista o diccionario
        # Actualizar el Treeview
        pass

# Crear la ventana principal y la instancia de la aplicación
root = tk.Tk()
app = AgendaApp(root)
root.mainloop()