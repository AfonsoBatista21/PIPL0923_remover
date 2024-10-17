def niveis(x):
    for i in range(1, x + 1):
       print(f" {i} " * i) 

n_niveis = int(input("Insira o número de níveis: "))
niveis(n_niveis)