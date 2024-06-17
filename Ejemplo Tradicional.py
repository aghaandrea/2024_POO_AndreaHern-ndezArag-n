def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    if not temperaturas:
        return 0
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Entrada de datos
temperaturas_tradicional = ingresar_temperaturas()

# Calculo y salida
promedio_tradicional = calcular_promedio_semanal(temperaturas_tradicional)
print(f"El promedio semanal de temperaturas es: {promedio_tradicional:.2f}°C")
