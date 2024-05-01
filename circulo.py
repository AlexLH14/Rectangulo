import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    @staticmethod
    def calcular_circulo():
        radio = float(input("Ingrese el radio del círculo: "))
        mi_circulo = Circulo(radio)
        print("\nÁrea del círculo:", mi_circulo.calcular_area())
        print("Perímetro del círculo:", mi_circulo.calcular_perimetro())

while True:
    Circulo.calcular_circulo()
    respuesta = input("¿Desea calcular el área y el perímetro de otro círculo? (s/n): ")
    if respuesta.lower() != 's':
        break
