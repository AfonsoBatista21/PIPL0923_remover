'''
file = open("demo.txt", "wt")

file.write("Linha 1\n")
file.write("Linha 2\n")
file.write("Linha 3\n")

print("done")
'''

'''
Crie uma app que peça ao utilizar os seus dedos e guarde esses dados num ficheiro de texto



deve utilizar o try/except para evitar erros
'''
myInfo = open("infos.txt", "wt")

nome= input("Nome:")
idade= input("Idade: ")
email= input("Email: ")

myInfo.write("")