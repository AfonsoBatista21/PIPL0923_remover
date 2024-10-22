def dado():
    try:
        nome = input("Insira o seu nome: ")
        idade = int(input("Insira sua idade: "))
        email = input("Insira o seu e-mail: ")

        file = open("dados.txt", "wt")

        file.write(nome)
        file.write(f"\n{idade}")
        file.write(f"\n{email}")


    except Exception as e:
        print(f"Erro. {e}")

dado()