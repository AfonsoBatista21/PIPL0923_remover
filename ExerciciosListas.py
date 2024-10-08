#1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

Lista = [
    int(input("Escreva o 1º valor:")),
    int(input("Escreva o 2º valor:")),
    int(input("Escreva o 3º valor:")),
    int(input("Escreva o 4º valor:")),
    int(input("Escreva o 5º valor:"))    
]
print(Lista)
#2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.´
lista2 = []

for i in range(10):
    novos = float(input("Digite um valor: "))
    lista2.append(novos)

print("\nLista com os valores adicionados: ")
lista2.sort(reverse = True)

print(lista2)
#3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista3=["nota1", "nota2", "nota3", "nota4"]

nota_1= float(input("Escreva a primeira nota: "))
nota_2= float(input("Escreva a segunda nota: "))
nota_3= float(input("Escreva a terceira nota: "))
nota_4= float(input("Escreva a quarta  nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

print(media)

#4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = []

vogais = "aeiou"


for i in range(10):
    letras = input(f"Escreva uma letra {i + 1}: ")

    if letras not in vogais:
        consoantes.append(letras)

print(f" Número de consoantes lidas: {consoantes}")
#5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
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
#6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numvetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
alunos = 10
notas = 4

medias = []
media_sete = 0

for i in range(alunos):
    media = 0
    for j in range(notas):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= alunos
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\nA média dos alunos foi:")
for i in range(alunos):
    print(f"Aluno {i+1}: {medias[i]}")

print(f"\n{media_sete} alunos tiveram média maior ou igual a 7.")
#7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

def multiplicacao(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado


vetor = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)


soma = sum(vetor)
multiplicacao_total = multiplicacao(vetor)


print(f"Números digitados: {vetor}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao_total}")
#8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []
n_pessoa = 1
for i in range (5):
    print('\nPessoa ', n_pessoa)
    ida = int(input('Digite a idade: '))
    alt = int(input('Digite a altura: '))
    idade.append(ida)
    altura.append(alt)
    n_pessoa += 1

idade.reverse()
altura.reverse()
print('\nIdade', idade,'\nAltura', altura)
#9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
import math
vetor = [1,2,3,4,5,6,7,8,9,10]
raizes = []

cont = 0
for i in range(len(vetor)):
    raiz = math.sqrt(vetor[cont])
    raizes.append(raiz)
    cont += 1

print('\nRaizes:\n',raizes)
print('\nSoma:\n',sum(raizes))
#10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
intercalada = []
contador = 0
for i in range(10):
    intercalada.append(A[contador])
    intercalada.append(B[contador])
    contador += 1
print(intercalada)
#11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
C = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
intercalada = []
contador = 0
for i in range(10):
    intercalada.append(A[contador])
    intercalada.append(B[contador])
    intercalada.append(C[contador])
    contador += 1
print(intercalada)
#12.Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random
idades = []
alturas = []
aluno_13 = []
media_13 = []

for i in range(30):
    numero_aleatorio = idades.append(random.randrange(1, 20))
    numero_aleatorio2 = alturas.append(random.randrange(50, 200))

for i in range(30):
    if idades[i] > 13:
        aluno_13.append(alturas[i])

media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        media_13.append(aluno_13[i])

print('\nA idade dos alunos são:\n',idades,'\nA altura dos alunos em cm são:\n',alturas)
print('\nForam ',len(aluno_13),' alunos com idade acima de 13 anos que são:\n',aluno_13)
print('\nA média de altura desses ',len(aluno_13),' alunos é:', media,'cm')
print('\nForam ',len(media_13),' alunos com mais de 13 anos possuem altura inferior à média de altura:\n',media_13)
#13.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperatura_meses = []
meses = ['Janeiro', 'Fevereiro', 'Março','Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print('\nMês de ', meses[i], ' :')
    media = temperatura_meses.append(float(input('Digite a temperatura média: ')))

media_anual = sum(temperatura_meses) / 12
print('\n' * 3)
for i in range(12):
    if temperatura_meses[i] > media_anual:
        print('Temperatura a cima da média no mês: ', meses[i])
'''
14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a - 'Telefonou para a vítima?'
    b - 'Esteve no local do crime?'
    c - 'Mora perto da vítima?'
    d - 'Devia para a vítima?'
    e - 'Já trabalhou com a vítima?' 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita', 
entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. 
Caso contrário, ele será classificado como 'Inocente'.
'''
sim = 0
perguntas = ['Telefonou para a vitima? [s/n]: ',
             'Esteve no local do crime? [s/n]: ',
             'Mora perto da vitima? [s/n]: ',
             'Devia para a vitima? [s/n]: ',
             'Já trabalhou com a vítima? [s/n]: '
             ]
for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if resposta == 's':
        sim += 1
if sim == 2:
    print('\nSuspeita!')
elif sim > 2 and sim <= 4:
    print('\nCumplice!')
elif sim == 5:
    print('\nAssassino!')
else:
    print('\nInocente!')
'''
15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
    a - Mostre a quantidade de valores que foram lidos;
    b - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d - Calcule e mostre a soma dos valores;
    e - Calcule e mostre a média dos valores;
    f - Calcule e mostre a quantidade de valores acima da média calculada;
    g - Calcule e mostre a quantidade de valores abaixo de sete;
    h - Encerre o programa com uma mensagem;
'''
valores = []
media_alta = []
valores_7 = []
cont = 1
rep = True

while rep != 0:
    print('\nValor nº ',cont) 
    val = (int(input('\nDigite o valor: ')))
    if val == -1:
       break
    else:
       valores.append(val)
    cont += 1

print('\n' * 2)
print('Quantidade de valores: \n',len(valores))
print('Os valores: \n',valores)
valores.reverse()                #invertendo a lista
print('Os valores na ordem inversa \n',valores)
print('A soma dos valores: \n',sum(valores))

media = sum(valores) / len(valores)
valores.reverse()                #invertendo novamente para a posição original

for i in range(len(valores)):
    if valores[i] > media:
        media_alta.append(valores[i])
    if valores[i] < 7:
        valores_7.append(valores[i])

print('A média dos valores: \n',media)
print('A quantidade de valores acima da média calculada: \n',media_alta)
print('A quantidade de valores abaixo de sete: \n',valores_7)
print('\nPrograma concluido!')

