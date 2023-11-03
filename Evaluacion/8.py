#En Python una clase es una estructura que se utiliza para organizar y encapsular datos y funciones relacionadas 
# en un solo objeto

#ejemplo


class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcular_area(self):
        return self.ancho * self.altura

rectangulo1 = Rectangulo(3, 7)

area = rectangulo1.calcular_area()
print("Área del rectángulo:", area)  
