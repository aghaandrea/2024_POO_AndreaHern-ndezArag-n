asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Asignaturas del curso:")
for asignatura in asignaturas:
    print(asignatura)

# Otra forma de imprimir la lista, menos legible para listas largas
# print(asignaturas)
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")  # Usando f-strings (Python 3.6+)

# Alternativa usando str.format():
# for asignatura in asignaturas:
#     print("Yo estudio {}".format(asignatura))
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    while True:  # Bucle para validar la entrada
        try:
            nota = float(input(f"Introduce la nota de {asignatura}: "))
            if 0 <= nota <= 10: # Valida que la nota esté entre 0 y 10
              break
            else:
              print("Por favor, introduce una nota entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")
    notas.append(nota)

print("\nNotas del curso:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
    numeros_ganadores = []

    print("Introduce los 6 números ganadores de la Lotería Primitiva (entre 1 y 49):")

    while len(numeros_ganadores) < 6:
        while True:
            try:
                numero = int(input(f"Introduce el número {len(numeros_ganadores) + 1}: "))
                if 1 <= numero <= 49 and numero not in numeros_ganadores:
                    numeros_ganadores.append(numero)
                    break
                elif numero in numeros_ganadores:
                    print("Este número ya ha sido introducido. Introduce un número diferente.")
                else:
                    print("Por favor, introduce un número entre 1 y 49.")
            except ValueError:
                print("Entrada inválida. Introduce un número entero.")

    numeros_ganadores.sort()  # Ordena la lista de menor a mayor

    print("\nNúmeros ganadores ordenados:")
    print(numeros_ganadores)

    # Opcional: Imprimir en formato más legible
    # print("Números ganadores ordenados:")
    # for numero in numeros_ganadores:
    #    print(numero, end=" ")
    # print() #Salto de línea final
    numeros = list(range(1, 11))  # Crea una lista con los números del 1 al 10
    numeros.reverse()  # Invierte el orden de la lista

    # Imprime los números separados por comas
    print(",".join(map(str, numeros)))

    # Otra forma (menos eficiente para listas muy grandes):
    # print(*numeros[::-1], sep=",")

    # Otra forma usando un bucle for (más control sobre el formato):
    # for i in range(len(numeros) -1, -1, -1):
    #     if i != 0:
    #         print(numeros[i], end=",")
    #     else:
    #         print(numeros[i])