#3/10/2024
#Condições / Controlo de fluxo

#boolean

'''

T e T -> T
T e F -> F
F e T -> T
F e F -> F




T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F


T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F



'''

ano = 2024


#if (se)
if ano == 2024:
    print("ano = 2024")
else:
    print("Outro ano")

print("fora do if")
#else if ( se não se )
#else ( se não)
#switch ( escolha )
#loops

#for (par)


#while ( enquanto - faça)

#Faça um programa que peça dois númros e imprima o maior deles
num1 = int(input("insira um numero: "))

num2 = int(input("insira ou numero: "))

if num1 > num2:
    print("O primeiro numero inserido é maior.")
else:
    print("O segundo numero inserido é maior")

#F e T -> F
num = 5
#F       and     T
if num % 2 == 0 and num % 5 == 0:
    print("par e div por 5")

else:
    print("impar ou não divisivel por 5")

num3 = 3
if num3 % 2 == 0:
    print("par ou div por 5")
elif num % 5 == 0:
    print("div por 5")
else:
    print("impar nem nao div por 5") 

'''
== <- comparações 


= <- atribuição


'''


letra = input("Digite a primeira letra do seu género (F ou M): ")

if letra == "F" or letra == "f":
    print("Feminino")
elif letra == "M" or letra =="m":
    print("Masculino")
else:
    print("Gênero Inválido")


#switch (escolha)
num = 0

match num:
    case 0:
        print("o num é 0")

    case 1:
        print("o num é 1")
    
    case 5:
        print("o num é 5")

    case _:
        print("Outro Valor")

menu = """
############Menu############
# OP1 ............ 1 #
# OP2 ............ 2 #
# OP3 ............ 3 #

 ########################"""
print(menu)

op = input("Selecione a op:")

match op:
    case "1":
        print("o num e 1")
    
    case "2":
        print("o num e 2")
    
    case "3":
        print("o num e 3")
        
    case _:
        print("outro valor")

#loops

#for (par)


#while ( enquanto - faça)

count = 0
while op != "q":
    op = input("Escreva o seu op: ")
    print("loop:", count)
    count =+ 1
    break
nun = 0

while num < 10:
    print(num)
    num += 1

#range
range(0,10,2)
'''
range(a,b,c)


a- LB


b- UB


c- step, se oculto c = 1


range(1,5)
1, 2, 3, 4,

range(5)
0, 1, 2, 3, 4

range(0, 11, 2)
0, 2, 4, 6, 8
'''
print("---" * 10)
for elm in range(0,100):
    print(elm)
    if elm %2 == 50:
        break
#for
nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",    "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

for nome in nomes:
    print(nome)

print("Fim do Loop")

print(nomes.count("Daniela"))

print(nomes.__len__())
print(len(nomes))
print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro" in nomes)

#nomes.sort(reverse=True)

print("-----------" * 5)
nomes.sort()
print(nomes)

'''
var
tipos de dados
type cast -int(""), str()
tuplos
op com var
if 
elif
else
and / or
match
while
for 
list
'''

while True:
    nota = input("Escreva um numero entre 0-10: ")
    try:
        nota = int(nota)
        if nota < 0 or nota > 10:
            print("Nota Invalida, escreva outro numero de 0-10.")
        else:
            print("Nota Valida")
            break
    except ValueError:
        print("Nota Invalida. Por favor, informe um número entre 0-10.")