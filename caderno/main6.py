from Quadrado import Quadrado

#q1 = Quadrado(20, "Amarelo")

#q2 = Quadrado(34, "Azul")

def Quadrados(lados):
    areas = {}
    for i, lado in enumerate(lados):
        area = lado ** 2
        areas[f'Quadrado {chr(65 + i)}'] = area  
    return areas


lados = [2, 3, 4, 5]


areas_quadrados = Quadrados(lados)


for quadrado, area in areas_quadrados.items():
    print(f'{quadrado}: Área = {area}')


print("")

def imprimir_triangulo(altura):
  for i in range(1, altura + 1):
    print(str(i) * i)


imprimir_triangulo(3)




