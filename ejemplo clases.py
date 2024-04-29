class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


def calcular_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    
    mi_rectangulo = Rectangulo(base, altura)

    print("Área del rectángulo:", mi_rectangulo.calcular_area())
    print("Perímetro del rectángulo:", mi_rectangulo.calcular_perimetro())


while True:
    calcular_rectangulo()
    respuesta = input("¿Desea calcular el área y el perímetro de otro rectángulo? (s/n): ")
    if respuesta.lower() != 's':
        break


'''crear un nuevo repositorio para esta practica
crear una nueva branch de la main
descargar github desktop para trabajar la rama de manera local
hacer algun cambio y subir con comandos'''
