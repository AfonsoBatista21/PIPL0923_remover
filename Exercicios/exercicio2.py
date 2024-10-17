def calcular_quadrados(l):
    areas = {}
    for i, lado in enumerate(l):
        area = lado ** 2
        areas[f'Quadrado {chr(65 + i)}'] = area
    return areas

l1 = [2, 3, 4, 5]

areas_quadrados = calcular_quadrados(l1)

for quadrado, area in areas_quadrados.items():
    print(f'{quadrado}: Área = {area}')


quadrado_maior = None
maior_area = 0

for quadrado, area in areas_quadrados.items():
    if area > area_maior:
        area_maior = area
        quadrado_area = quadrado

print(f'\nO quadrado com a maior área é o {quadrado_maior}')