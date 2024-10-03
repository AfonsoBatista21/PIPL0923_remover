#1.Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))

if num1 > num2:
    print("O maior numero é: ", num1)
else:
    print("O maior numero é: ", num2)


#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = int(input(" Escreva um numero: \n "))

if n1 > 0:
	print(f"{n1} o teu numero é positivo.")
elif n1 < 0:
	print(f"{n1} o teu numero é negativo.")
else: 
	print("Numero não é compativel")
	
#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input("Digite a primeira letra do seu género (F ou M): ")

if letra == "F" or letra == "f":
    print("Feminino")
elif letra == "M" or letra =="m":
    print("Masculino")
else:
    print("Gênero Inválido")
#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra1 = input(" Digite uma letra: \n   ")

if letra1.lower() == "a" or letra1.lower() == "e" or letra1.lower() == "i" or letra1.lower() == "0" or letra1.lower() == "u":
	print(f"'{letra1}' é uma vogal.")
elif letra1.isnumeric():
	print(f"Porfavor insira letras, '{letra1}' é um número.")
else:
	print(f"'{letra1}' é uma consoante.")
	
#5.
nu1 = float(input("Digite a primeira nota: \n   "))
nu2 = float(input("Digite a segunda nota: \n   "))

media = (nu1+nu2)/2
print(f"Sua média foi: {media}")
if media == 10:
	print("Aprovado com distinção")
elif media < 7:
	print("Reprovado.")
else:
	print("Aprovado")
#6
a = float(input("Digite o primeiro número: \n   "))
b = float(input("Digite o segundo: \n   "))
c = float(input("Mais um número: \n   "))

if a>b:
	if a>c:
		print(f"{a} é o maior")
	else:
		print(f"{c} é o maior")
elif b>c:
	print(f"{b} é o maior")
else:
	print(f"{c} é o maior")
#7.
if a>b:
	if a>c:
		print(f"{a} é o maior número.")
	else:
		print(f"{c} é o maior número.")
elif b>c:
	print(f"{b} é o maior número.")
else:
	print(f"{c} é o maior número.")

if a<b:
	if a<c:
		print(f"{a} é o menor número.")
	else:
		print(f"{c} é o menor número.")
elif b<c:
	print(f"{b} é o menor número.")
else:
	print(f"{c} é o menor número.")
#8.
print(" - Que produto devo comprar? -")
input("1. Qual o ponto forte do primeiro produto? \n > ")
v1 = float(input("1. Valor do primeiro produto: \n  > R$ "))
input("2. Qual o ponto forte do segundo produto? \n > ")
v2 = float(input("2. Valor do segundo produto: \n  > R$ "))
input("3. Qual o ponto forte do terceiro produto? \n > ")
v3 = float(input("3. Valor do terceiro produto: \n  > R$ "))

if v1<v2:
	if v1<v3:
		print("O primeiro produto é o melhor!")
	else:
		print("O terceiro produto é o melhor!")
elif v2<v3:
	print("O segundo produto é o melhor!")
else:
	print("O terceiro produto é o melhor!")
#9.
a = float(input("Digite um número: \n > "))
b = float(input("Digite outro número: \n > "))
c = float(input("Mais um número: \n > "))

if a>b:
	if a>c: 
		if b>c:
			print(f"Em ordem decrescente, fica:\n{a}\n{b}\n{c}")
		else:
			print(f"Em ordem decrescente, fica:\n{a}\n{c}\n{b}")
	else:
		print(f"Em ordem decrescente, fica:\n{c}\n{a}\n{b}")
elif b>c:
	if a>c:
		print(f"Em ordem decrescente, fica:\n{b}\n{c}\n{a}")
	else:
		print(f"Em ordem decrescente, fica:\n{b}\n{a}\n{c}")
else:
	print(f"Em ordem decrescente, fica:\n{c}\n{b}\n{a}")

#10.
print("Pertences a que turno?")
print("""
	M - Matutino
	V - Vespertino
	N - Noturno
""")
turno = input(":")

if turno.lower() == "m":
	print("Bom dia!")
elif turno.lower() == "v":
	print("Boa tarde")
elif turno.lower() == "n":
	print("Boa noite")
else:
	print("Valor inválido.")
#11
salBruto = float(input("Informe seu salário atual: \n > R$ "))

if salBruto<=280:
	percent = 0.2
	aumento = salBruto * percent
	salNovo = salBruto + aumento

elif salBruto <=700:
	percent = 0.15
	aumento = salBruto * percent
	salNovo = salBruto + aumento

elif salBruto < 1500:
	percent = 0.1
	aumento = salBruto * percent
	salNovo = salBruto + aumento
else:
	percent = 0.05
	aumento = salBruto * percent
	salNovo = salBruto + aumento

print(f"Salário antigo:        : R$ {salBruto:.2f}")
print(f"Percentual aplicado    :    {percent * 100} %")
print(f"Valor do aumento       : R$ {aumento:.2f}")
print(f"Novo salário           : R$ {salNovo:.2f}")
#12
quantHoras = float(input("Quantidade de horas trabalhadas por mês: \n  "))
valorHora = float(input("Valor da hora: \n  R$ "))
sind = input("É adepto do sindicato? (S/N) \n  ")

salbruto = valorHora * quantHoras
somador = 0
print(f"\n\nSalário Bruto: ({valorHora} * {quantHoras})      : R$ {salbruto:.2f}")


ir = 0
if salbruto <=900:
	pass
elif salbruto <=1500:
	percent = 0.05
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
elif salbruto <=2500:
	percent = 0.1
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
else:
	percent = 0.2
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
somador = somador + ir


s=0
if sind.lower() == "s":
	percent = 0.3
	s = salbruto * percent
	print(f"(-) Sindicato ({percent*100}%)              : R$ {s:.2f}  ")
somador = somador + s


percent = 0.1
inss= salbruto * percent
print(f"(-) INSS ({percent*100}%)                  : R$ {inss:.2f}")
somador = somador + inss


percent = 0.11
fgts= salbruto * percent
print(f"FGTS ({percent*100}%)                      : R$ {fgts:.2f}")


salL = salbruto - somador
print(f"Total dos descontos               : R$ {somador:.2f}")
print(f"Salário Liquido                   : R$ {salL:.2f}")
#13
semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
count = 1
num = float(input("Escreva um número: \n "))

if num < 0 or num > 8:
	print("Numero inválido!")
else:
	for dia in semana:
		if count == num:
			print(f"O número que você escrevou é o dia da semana: {dia}.")
		count += 1
#14
nn1 = float(input("Digite a primeira nota: \n   "))
nn2 = float(input("Digite a segunda nota: \n   "))

media = (nn1+nn2)/2
print(f"A tua média foi: {media}")
if media <=4:
	conceito = "E"
elif media <= 6:
	conceito = "D"
elif media <=7.5:
	conceito = "C"
elif media <=9:
	conceito = "B"
else:
	conceito="A"

if conceito=="E" or conceito =="D":
	print(f"A tua nota foi {conceito}, então, reprovado.")
else:
	print(f"A tua nota foi {conceito}, então, aprovado.")
#15
lado1 = float(input("Digite o valor do primeiro lado: \n  "))
lado2 = float(input("O valor do segundo: \n   "))
lado3 = float(input("Do terceiro agora: \n   "))

if lado1 == lado2 and lado2 == lado3:
	print("Esses dados são de um triângulo equilátero.")
elif lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
	if lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
		print("Esses dados são de um triângulo isósceles.")
	else:
		print("Esses dados são de um triângulo escaleno.")
else:
	print("Esses dados não podem formar um triângulo.")
#16
import math
print("Informe os valores de A, B, e C, seguindo esta ordem.")
a = float(input("Valor de A: \n   "))
if a == 0:
	print("Se o valor de A é zero, essa não é uma equação de segundo grau,\ne portanto não será resolvida aqui.")
else:
	b = float(input("Valor de B: \n   "))
	c = float(input("Valor de C: \n  "))

	delta=math.pow(b,2)-(4*a*c)

	if delta < 0:
		print("Essa equação não tem resultados reais. Delta deu um valor negativo. ")
		print(f"Delta = {delta}")
	elif delta ==0:
		print("Essa equação terá somente um resultado real.")
		print(f"Delta = {delta}")
		raiz = ((-b) - math.sqrt(delta))/(2*a)
		print(f"A raiz dessa equação é:\nR1 = {raiz}\nR2 = R1")
	else:
		print("Essa equação terá dois resultados reais. Delta deu um valor positivo. ")
		print(f"Delta = {delta}")
		raiz1 = ((-b) - math.sqrt(delta))/(2*a)
		raiz2 = ((-b) + math.sqrt(delta))/(2*a)
		print(f"As raizes dessa equação são:\nR1 = {raiz1}\nR2 = {raiz2}")

#17
ano = str(input("Digite um ano e descubra se ele foi/será bissexto: \n  > "))
tamanho = len(ano)

ano=int(ano)

oFinal=ano%100

if oFinal == 00:

	if ano%400 == 0:
		print("Esse ano foi/será bissexto!")
	else:
		print("Esse ano não foi/será bissexto!")
else:

	if oFinal%4 == 0:
		print("Esse ano foi/será bissexto!")
	else:
		print("Esse ano não foi/será bissexto!")
		
#18
print("Digite uma data qualquer:")
dia = int(input("Dia (dd): \n  > "))
mes = int(input("Mês (mm): \n  > "))
ano = int(input("Ano (aaaa): \n  > "))

valida = False

if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
	if dia <=31 and dia > 0:
		valida=True
elif mes != 2:
	if dia <=30  and dia > 0:
		valida = True
else:
	if ano%4==0 or ano%400==0:
		if dia<=29 and dia > 0:
			valida = True
	else:
		if dia<=28 and dia > 0:
			valida = True

if valida:
	print(f"É uma data válida!\n{dia:02d}/{mes:02d}/{ano}")
else:
	print("Data invalida")
#19
SEP=", "
END=".\n"


print(" - Centenas, dezenas e unidades -")
print("Para números com 3 dígitos")
num = int(input("Insira o número para ser analisado: \n  > "))

if num < 1000 and num > -1000:
	unidade = num % 10
	dezena = num //10 %10
	centena=num//100%10

	if centena == 0:
		c = None
	else:
		if centena == 1:
			c = " 1 centena"
		else:
			c = f" {centena} centenas"

	if dezena == 0:
		d = None
	else:
		if dezena == 1:
			d = "1 dezena"
		else:
			d = f"{dezena} dezenas"
		
	if unidade == 0:
		u = None
	else:
		if unidade == 1:
			u = "1 unidade"
		else:
			u = f"{unidade} unidades"

	if c:
		if d:
			if u:
				print(f"{num} = {c}", f"{d}", f"{u}", sep=SEP, end=END)
			else:
				print(f"{num} = {c}", f"{d}", sep=SEP, end=END)
		elif u:
			print(f"{num} = {c}", f"{u}", sep=SEP, end=END) 
		else:
			print(f"{num} = {c}", sep=SEP, end=END)
	elif d:
		if u:
			print(f"{num} = {d}", f"{u}", sep=SEP, end=END)
		else:
			print(f"{num} = {d}", sep=SEP, end=END)
	elif u:
		print(f"{num} = {u}", sep=SEP, end=END)
	else:
		print("O número digitado foi 0. Não tem nada.")

else:
	print("Número inválido. Tente novamente!")
#20
nm1 = float(input("Digite a primeira nota: \n  > "))
nm2 = float(input("Digite a segunda nota: \n  > "))
nm3 = float(input("Digite a terceira nota: \n  > "))

media = (nm1+nm2+nm3)/3
print(f"Sua média foi: {media:.2f}")
if media == 10:
	print("Aprovado com distinção! Não fez mais que sua obrigação.")
elif media < 7:
	print("Reprovado.!")
else:
	print("Aprovado! Continue assim!")
#21
notas=[]
print("- Notas disponíveis: 1, 5, 10, 50 e 100 -")
valor = int(input("Valor para saque: \n  > "))
resto=valor #sem essa linha, valores menores que 100 dão erro

if valor >= 10 and valor <=600:
	quant = valor//100
	if quant!=0:
		resto = valor%100
		if quant ==1:
			notas.append(f"1 nota de 100")
		else:
			notas.append(f"{quant} notas de 100")
		
	quant = resto//50
	if quant!=0:
		resto = valor%50
		if quant ==1:
			notas.append(f"1 nota de 50")
		else:
			notas.append(f"{quant} notas de 50")
		
	quant = resto//10
	if quant!=0:
		resto = valor%10
		if quant ==1:
			notas.append(f"1 nota de 10")
		else:
			notas.append(f"{quant} notas de 10")

	quant = resto//5
	if quant!=0:
		resto = valor%5
		if quant ==1:
			notas.append(f"1 nota de 5")
		else:
			notas.append(f"{quant} notas de 5")

	quant = resto//1
	if quant!=0:
		resto = valor%1
		if quant ==1:
			notas.append(f"1 nota de 1")
		else:
			notas.append(f"{quant} notas de 1")

	x=1
	print("Vais receber:", end=" ")
	for i in notas:
		if x==1:
			print(i, end=".")
		else:
			print("\b, ",i, end=".")
		x+=1
	print("")
else: 
	print("Valor inválido.")
#22
print(" - Par ou ímpar? -")
nmr = float(input("Digite um número para ser analisado: \n  > "))

if nmr == 0:
	par = True
else:
	if nmr%2==0:
		par=True
	else:
		par=False

if par:
	print("Número é par!")
else:
	print("Número é ímpar!")
#23
a = float(input("Digite um número para ser analisado: \n  > "))

b=int(a)
if a==b:
	print("É um número inteiro.")
else:
	print("É um número decimal.")
#24
a = float(input("Digite um número para ser analisado: \n  > ")) #recebe o primeiro número
b = float(input("Digite outro número para ser analisado: \n  > ")) # recebe o segundo


print(f" | Os números foram: {a} e {b}    ") 
print(" | Escolha o teste a ser feito:  ")
print(" | [1] - Par ou Ímpar             |")
print(" | [2] - Positivo ou Negativo     |")
print(" | [3] - Inteiro ou decimal       |")

opc = int(input("\n > "))


if opc == 1:

    if a == 0:
        par = True
    else:
        if a%2==0:
            par=True
        else:
            par=False

    if par:
        print(f"{a} é par!")
    else:
        print(f"{a} é ímpar!")

    if b == 0:
        par = True
    else:
        if b%2==0:
            par=True
        else:
            par=False

    if par:
        print(f"{b} é par!")
    else:
        print(f"{b} é ímpar!")
elif opc==2:

    if a > 0:
        print(f"{a} é um número positivo.")
    elif a < 0:
        print(f"{a} é um número negativo.")
    else: 
        print("Numero Invalido")
   
    if b > 0:
        print(f"{b} é um número positivo.")
    elif b < 0:
        print(f"{b} é um número negativo.")
    else: 
        print("Numero Invalido")
elif opc==3:

    aux=int(a)
    if a==aux:
        print(f"{a} é um número inteiro.")
    else:
        print(f"{a} é um número decimal.")

    aux=int(b)
    if b==aux:
        print(f"{b} é um número inteiro.")
    else:
        print(f"{b} é um número decimal.")
else:
 
    print("Opção não disponível")
#25
lista=[]
resposta = input("Telefonou para a vítima? (S/N): \n  > ")

if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Esteve no local do crime? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Mora perto da vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Devia para a vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Já trabalhou com a vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)

tamanho = len(lista)


if tamanho == 5:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado culpado!")
elif tamanho >=3:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado cúmplice!")
elif tamanho ==2:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado suspeito!")
else:
    print(f"Por responder que sim a {tamanho} perguntas, você está liberado!")
