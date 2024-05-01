import math

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
class Menu:

    def calcular_rectangulo(self):
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        
        mi_rectangulo = Rectangulo(base, altura)

        print("\n Área del rectángulo:", mi_rectangulo.calcular_area())
        print("Perímetro del rectángulo:", mi_rectangulo.calcular_perimetro())

    def calcular_circulo(self):
        radio = float(input("Ingrese el radio del círculo: "))
        mi_circulo = Circulo(radio)
        print("\n Área del círculo:", mi_circulo.calcular_area())
        print("Perímetro del círculo:", mi_circulo.calcular_perimetro())
    
    def seleccionar(self):
        print("\nMENU:")
        print("1. Calcular área y perímetro de un rectángulo")
        print("2. Calcular área y perímetro de un círculo")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3):\n ")
        if opcion == '1':
            self.calcular_rectangulo()
        elif opcion == '2':
            self.calcular_circulo()
        elif opcion == '3':
            print("¡Hasta luego!")
            return False
        else:
            print("Opción no válida. Selecciona una opción válida.")

menu = Menu()

for intento in range(5):
    if menu.seleccionar():
        break
   

    
