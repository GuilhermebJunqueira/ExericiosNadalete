op = 0
c = 0
d = 0
posmenor = 0
posmaior = 0
dados1 = [""] * 50
dados2 = [""] * 50
dados3 = [""] * 50
nome = ""
milha = [0.0] * 50
milhas = 0.0

while op != 6:
    print("\n********************")
    print(" * MENU *")
    print(" ********************")
    print(" 1 - Cadastra dados do cliente")
    print(" 2 - Cadastra milhagem do cliente")
    print(" 3 - Lista milhagem do cliente")
    print(" 4 - Imprime os nomes que têm maior e menor milhagem")
    print(" 5 - Imprime os nomes e as milhagens")
    print(" 6 - SAIR")
    op = int(input("OPCAO: "))

    if op == 1:
        if c <= 49:
            print(f"{c + 1} - nome: ", end="")
            dados1[c] = input()
            print("endereco: ", end="")
            dados2[c] = input()
            print("telefone: ", end="")
            dados3[c] = input()
            c += 1
        else:
            print("Arquivo cheio")

    elif op == 2:
        print("Nome para procura: ", end="")
        nome = input()
        d = 0
        while d < c - 1 and nome != dados1[d]:
            d += 1
        if nome == dados1[d]:
            print(f"Digite milhagem de {dados1[d]}: ", end="")
            milhas = float(input())
            milha[d] -= milhas
        else:
            print("Nome não encontrado")

    elif op == 3:
        print("Nome para procura: ", end="")
        nome = input()
        d = 0
        while d < c - 1 and nome != dados1[d]:
            d += 1
        if nome == dados1[d]:
            print(f"Milhagem de {dados1[d]}: {milha[d]}")
        else:
            print("Não encontrado")

    elif op == 4:
        d = 1
        posmenor = 0
        posmaior = 0
        while d < c:
            if milha[d] > milha[posmaior]:
                posmaior = d
            else:
                if milha[d] < milha[posmenor]:
                    posmenor = d
            d += 1
        print("\nDados da pessoa de maior milhagem")
        print(f"Nome: {dados1[posmaior]}")
        print(f"Endereco: {dados2[posmaior]}")
        print(f"Telefone: {dados3[posmaior]}")
        print(f"Milhagem: {milha[posmaior]}\n")
        print("Dados da pessoa de menor milhagem")
        print(f"Nome: {dados1[posmenor]}")
        print(f"Endereco: {dados2[posmenor]}")
        print(f"Telefone: {dados3[posmenor]}")
        print(f"Milhagem: {milha[posmenor]}\n")

    elif op == 5:
        print("\nListagem")
        for d in range(c):
            print(f"{d + 1} - {dados1[d]}: {milha[d]}")

    elif op == 6:
        print("BOA VIAGEM")

    else:
        print("Opcao inexistente")

print()
