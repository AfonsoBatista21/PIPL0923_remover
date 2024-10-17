def letras(string) -> str:
    repetição = {}
    for elm in string:
        if elm.isalpha():  
            if elm in repetição:
                repetição[elm] += 1
            else:
                repetição[elm] = 1
    return repetição

resultado = letras("adjadudahsdahsdhahde")
print(resultado)
