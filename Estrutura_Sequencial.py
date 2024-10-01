#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Ola mundo")
#2 e 3 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. Faça um Programa que peça dois números e imprima a soma.
primeironum =int(input("Escreva o primeiro numero:"))

segundonum =int(input("Digite o segundo numero:"))

soma = primeironum + segundonum

print("A adição dos 2 numeros da: \n", soma)

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1= float(input("Escreva a primeira nota: "))
nota_2= float(input("Escreva a segunda nota: "))
nota_3= float(input("Escreva a terceira nota: "))
nota_4= float(input("Escreva a quarta  nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

print("A media das notas e:", media)
#5 Faça um Programa que converta metros para centímetros.
conversao = float(input("Insira a sua medida em metros: \n"))

centimetros = conversao * 100;

print("A sua conversão deu: \n", centimetros)
#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("O Raio do circulo:"))

area = 3.14 * (raio ** 2)

print("Área do circulo é:", area)
#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("\nInsira a medida do lado do quadrado em metros:"))

area = lado * lado
print("Dobro da area do quadrado: %.2f m2 " %(area*2))
#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario_h = float(input('Quanto ganhas por hora: '))
num_h = int(input('Quantas horas por mês: '))
salario = salario_h * num_h
print('Salario: R$ ', salario)
#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
Temp = float(input("Temperatura em Fahrenheit:"))
print("Temperatura em Celcius: %.2f" %(5/9 * (Temp-32)))
#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Temp_C = float(input('Temperatura em Celsius'))
print('Temperatura em Fahrenheit: %.2f' %(9*Temp_C/5 + 32))
#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
n1 = int(input('1º Número inteiro: '))
n2 = int(input('2º Número inteiro: '))
n3 = float(input('Número real: '))

print ('Soma:', ((2*n1) * (n2/2)))
print ('Produto:', (3 * n1) + n3)
print ('Cubo:', n3**3)
#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Altura:"))
print ("Peso ideal:", (72.7*altura) -58)
#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))
#14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso_1 = float(input('Peso:'))
if peso_1 > 50:
	excedente = peso_1 - 50
	multa = excedente * 4
else:
	excedente = 0
	multa = 0
print ('Peso: %.2f Kg' %peso)
print ('Excesso: %.2f Kg' %excedente)
print ('Multa: R$ %.2f' %multa)
#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
vh = float(input('Valor da hora:'))
qh = int(input('Quantidade de horas trabalhadas:'))

salario_bruto = vh * qh
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print (' + Salário Bruto: R$ %.2f' %salario_bruto)
print (' - IR: R$ %.2f' %ir)
print (' - INSS: R$ %.2f' %inss)
print (' - Sindicato: R$ %.2f' %sindicato)
print (' = Salário Liquido: R$ %.2f' %salario_liquido)

#18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))