
import random

quadrados=[]

for quadrado in range(400):
    lado = random.randint(1, 50)
    area = lado ** 2
    quadrados.append((lado,area))

maior_area = quadrados[0]
menor_area = quadrados[0]

for quadrado in quadrados:
    if quadrado[1] > maior_area[1]:
        maior_area = quadrado
    if quadrado[1] < menor_area[1]:
        menor_area = quadrado

print("Quadrado com a maior área:")
print(f"Lado: {maior_area[0]}, Área: {maior_area[1]}")

print("\nQuadrado com a menor área:")
print(f"Lado: {menor_area[0]}, Área: {menor_area[1]}")
