#tuple

tp1 = ("Afonso","ATEC", 10793)
print(tp1[0])
print(tp1[1])
print(tp1[2])

#print(tp1[3]) <- Erro

#tp1[0]= "Novo Nome"
list_temp = list(tp1)
print(list_temp)

list_temp[0] = "Novo Nome"
tp1 = tuple(list_temp)

print(tp1)

print("----Unpack----")
tp1 = ("Afonso","ATEC", 10793)

(nome, Escola, UFCD) = tp1

print(nome)
print(Escola)
print(UFCD)

nome = "Novo nome 2"

print("---unpack list---")
tp1 = ("Afonso","ATEC", 10793)
temp_list = list(tp1)
print(type(temp_list))
(nome, Escola, UFCD) = temp_list

print(nome)
print(Escola)
print(UFCD)

print("----metodos tuple----")
tp1 = ("Afonso","ATEC", 10793, "Afonso")
print(tp1.count("Afonso"))
#Listas
#listas (arrays)
print("--- listas (arrays) ---")

#lista vs array

my_list = ["Gonçalo", "Ana", "Rita", "Luiz"]

print(my_list)
print(my_list[0])
print(my_list[1])

my_list[0] = "Novo nome"

print(my_list[0])
print(my_list)

nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana", "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

print(nomes[0])
print(nomes[0:5]) # nomes[n:m] -> n a m -1

print(nomes[-10:-5])

arr = [
    input("Introduza o valor 1: "),
    input("Introduza o valor 2: "),
    input("Introduza o valor 3: "),
    input("Introduza o valor 4: "),
    input("Introduza o valor 5: "),
]
print(arr)

valor= int(input("Quantos valores pretende adicionar? "))


lista = []


for i in range(valor):
    valor = input(f"Digite o valor {i+1}: ")
    lista.append(valor)


print("Os valores na lista são:", lista)
#S
numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print("Todos os números:", numeros)
print("Os números pares são:", par)
print("Os números ímpares são:", impar)

def receber_notas():
    notas = []
    num_notas = int(input("Quantas notas você deseja adicionar? "))
    
    for i in range(num_notas):
        while True:
            try:
                nota = float(input("Digite uma nota (0 a 20): "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Por favor, insira uma nota entre 0 e 20.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")
    
    print("Notas adicionadas:", notas)

receber_notas()
#Set
from time  import sleep
import random

mySet = {"val1", "val2", "val3", "val4"}
print(mySet)

"""
run 1: {"val2",'val1', 'val3','val4'}
run 1: {"val1",'val2', 'val4','val3'}
run 1: {"val1",'val2', 'val4','val3'}
run 1: {"val4",'val2', 'val1','val3'}
"""
for i in mySet:
    print(i)

print("----" * 3)

mySet = {"val1", "val2", "val3", "val4"}
print(mySet)

mySet.add("val15")
print(mySet)

mySet.add("val3")
print(mySet)

lista = list()

listNum = set()
for _ in range(1000):
    #sleep(0.01)
    i = random.randint(  0,  1000)
    listNum.add(i)



#input("continuar? ")
print(listNum.len())

print("----" * 3)
print("----" * 3)

mySet = {"val1", "val2", "val3", "val4"}


print("val19" in mySet)
mySet.remove("val2")

print(mySet)
mySet2 = {"val5", "val", "val3", "val4"}

#mySet.remove("val2")

print("----" * 3)
print("----" * 3)


mySet = {"val1", "val2", "val3", "val4"}
mySet = {"val5", "val", "val3", "val4"}

#uniao

""
print("---" * 3,"union", "---" * 3)
resp = mySet.union(mySet2)
print(resp)

#interceção
print("---" * 3,"intercação", "---" * 3)
resp = mySet.intersection(mySet2)
print(resp)

#diferença
print("---" * 3,"diferença", "---" * 3)
resp = mySet.difference(mySet2)
print(resp)

resp = mySet2.difference(mySet)
print(resp)

#diferencia simetrica

resp = mySet.symmetric_difference(mySet2)
print(resp)
#dict