import random
#Crie um dicionario dinâmico onde pergunta ao utilizador quantos valores quer adicionar 
#em seguida deve pedir ao utilizador os dados as keys e valores que quer adicionar os respectivos valores

dici = {}


num_valores = int(input("Quantos valores quer adicionar? "))


for _ in range(num_valores):
    chave = input("Insira a chave: ")
    valor = input("Insira o valor: ")
    dici[chave] = valor

print(dici)