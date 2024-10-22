'''
quadrado 
lado: int
cor str

'''

class Triangulo:
      def __init__(self, base, altura, cor):
            self.base = base
            self.altura = altura
            self.cor = cor

class circulo:
      def __init__(self, raio, cor):
            self.raio = raio
            self.cor = cor

class Trapezio:
      def __init__(self, basebig, basesmall, altura2,cor):
        self.basebig = basebig
        self.basesmall = basesmall
        self.altura2 = altura2
        self.cor = cor 

"""
Quadradro
    lado: int
    cor: str

"""
class Quadrado:

    def init(self, lado: int, cor: str):
        self.lado = lado
        self.cor = cor



    def area(self) -> int:
        area = self.lado * self.lado
        return area




    def perimetro(self):
        perimetro = self.lado *4
        return perimetro

    def mudar_cor(self, nova_cor: str):
        self.cor = nova_cor
