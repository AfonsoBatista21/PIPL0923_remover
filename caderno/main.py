#cmt

"""
cmt
varias
linhas
"""

#prt
print("Ola mundo")


#var
nome = "Valor" # String (cadeia de caracteres)
idade = 10 # max int em c -> 2,147,482,647, max int em Py -> não existe
nota = 10.9 # Float( 6 a 7 casas decimais ) e double (14)
aprovado = True # 


print(nome)
nome = 10 
print(nome)


soma = idade + 3
print(soma)


soma2 = nota + 2
print(soma2)


nome = "Valor"
soma3 = nome + "Foo"
print(soma3)


nome = "Valor"
#soma4 = nome + 2024
#print(soma4)


op5 = nome * 2
print(op5)

#print v2


nome = "Afonso"
ano = 2024

"Ola Mundo, Afonso em 2024"
#str(ano) converte para string 

print("Ola mundo,",  nome  ,"em" , str(ano))

print("Ola mundo,"+  nome  + "em" + str(ano))

print("Ola mundo,",  nome  ,"em" ,ano)

print(f"Ola mundo, {nome.upper()} em {ano}")


#-> % <-
op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)


op2 = 10 / 3
print(op2)


op2 = 10 // 3
print(op2)


#ler dados do teclado

nome2 = input("Digite seu nome: ")
print(f"ola, nome2")