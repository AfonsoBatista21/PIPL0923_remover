def palavras(string:str):
    letras = string.split(" ")
    elm = {}
    for word in letras:
        if elm.get(word) != None:
            elm[word] = elm[word]+1
        else:
            elm[word] = 1
    return elm
res = palavras("bom dia bom dia chefe")
print(res)