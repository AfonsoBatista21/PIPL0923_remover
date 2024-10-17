import random

print(random.randint(a=1,b=10000))

#Crie uma lista com 100 numeros inteiros aleatorios
#imprima o valor todos os valores da lista multiplicados pelo posição
#Exemplo:
#lista -> [3,4,5,10]
#ouput:
#0
#4
#10
#30
list=[]
for a in range(1000):
    list.append(random.randint(1,1000)*a)
    print(list)


