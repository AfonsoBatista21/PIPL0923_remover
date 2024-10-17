def ola_mundo():
    print("Ola mundo")

ola_mundo()
ola_mundo()
ola_mundo()
ola_mundo()

def ola_mundo_v2(nome):
    print(f"Ola mundo, {nome}")

ola_mundo_v2("Afonso")
ola_mundo_v2("Rui")
ola_mundo_v2("Ana")

num = 12

def ola_mundo_v3(nome: str, ano: int, idade:int):
    print(f"Ola mundo, {nome}, {ano}")

ola_mundo_v3(nome="Afonso", ano=2000, idade=88)

def soma(valor1:int, valor2:int) -> int:
    return valor1 + valor2

res = soma(valor1=3,valor2=4)
print(res)


res2 = soma(valor1=3.5,valor2=4.5)
print(res2)


res3 = soma(valor1="3.5",valor2="4.5")
print(res3)


