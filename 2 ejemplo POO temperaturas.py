class ClimaSemana:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio_semanal(self):
        if not self.temperaturas:
            return 0
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

# Creación de objeto
clima_poo = ClimaSemana()

# Entrada de datos
clima_poo.ingresar_temperaturas()

# Cálculo y salida
promedio_poo = clima_poo.calcular_promedio_semanal()
print(f"El promedio semanal de temperaturas es: {promedio_poo:.2f}°C")