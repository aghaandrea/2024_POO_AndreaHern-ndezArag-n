class Carro:
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None  # Inicialmente, el carro no tiene conductor

    def asignar_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona

    def __str__(self):
        return f'Carro {self.modelo} del año {self.anio}, conducido por {self.conductor.nombre if self.conductor else "nadie"}.'

class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Persona {self.nombre} con licencia número {self.licencia}.'

# Creación de objetos
carro1 = Carro('Peugeot', 2018)
carro2 = Carro('Chery', 2023)
persona = Persona('José David', 'B')

# Asignar un conductor al carro
carro1.asignar_conductor(persona)

# Ejemplo de salida
print(carro1)  # Debería imprimir: Carro Peugeot del año 2018, conducido por José David.
print(carro2)  # Debería imprimir: Carro Chery del año 2023, conducido por nadie.
print(persona)  # Debería imprimir: Persona José David con licencia número B.