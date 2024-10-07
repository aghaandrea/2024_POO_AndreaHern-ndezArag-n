import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Crear los elementos de la interfaz
entrada_tarea = tk.Entry(ventana)
lista_tareas = tk.Listbox(ventana)
boton_agregar = tk.Button(ventana, text="Agregar")
boton_marcar = tk.Button(ventana, text="Marcar como Completada")
boton_eliminar = tk.Button(ventana, text="Eliminar")

# Posicionar los elementos en la ventana
# ... (Utilizar grid, pack o place)

# Función para agregar una nueva tarea
def agregar_tarea():
    nueva_tarea = entrada_tarea.get()
    # Agregar la nueva tarea a la lista
    lista_tareas.insert(tk.END, nueva_tarea)
    entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para marcar una tarea como completada
def marcar_como_completada():
    # Obtener el índice de la tarea seleccionada
    indice = lista_tareas.curselection()
    # Marcar la tarea como completada (por ejemplo, cambiando el color del texto)

# Función para eliminar una tarea
def eliminar_tarea():
    # Obtener el índice de la tarea seleccionada
    indice = lista_tareas.curselection()
    # Eliminar la tarea de la lista

# Vincular los botones con las funciones
boton_agregar.config(command=agregar_tarea)
boton_marcar.config(command=marcar_como_completada)
boton_eliminar.config(command=eliminar_tarea)

# Vincular los atajos de teclado a las funciones
ventana.bind("<Return>", agregar_tarea)
ventana.bind("c", marcar_como_completada)
ventana.bind("d", eliminar_tarea)
ventana.bind("<Escape>", lambda e: ventana.quit())

# Iniciar el bucle principal de la aplicación
ventana.mainloop()