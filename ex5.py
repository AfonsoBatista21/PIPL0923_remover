#crie uma funçãp que some todos os valores de uma lista de inteiros

def soma_lista(lista) -> int:
    soma = 0
    for num in lista:
        soma += num
    return soma