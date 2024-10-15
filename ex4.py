
valores = []


for _ in range(10):
    valor = input("Insira um valor numérico: ")
    if valor.isdigit():
        valores.append(int(valor))
    else:
        print(f"Valor '{valor}' descartado, não é numérico.")


if valores:
    media = sum(valores) / len(valores)
    print(f"A média dos valores na lista é: {media}")
else:
    print("Nenhum valor numérico foi inserido.")
