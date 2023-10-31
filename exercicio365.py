num = []
valor = []
destino = []
data = []

print("Número de cheques do talonário:")
nc = int(input())

for k in range(nc):
    print(f"Número do cheque {k + 1}:")
    num.append(input())
    print(f"Valor do cheque {k + 1}:")
    valor.append(input())
    print(f"Data do cheque (ddmmaa) {k + 1}:")
    data.append(input())
    print(f"Destino do cheque {k + 1}:")
    destino.append(input())

print("\nRELACAO dos CHEQUES\n")
for k in range(nc):
    print(f"Número do cheque: {num[k]}")
    print(f"Valor do cheque: {valor[k]}")
    print(f"Data do cheque: {data[k]}")
    print(f"Destino do cheque: {destino[k]}\n")
    
    if k < nc - 1:
        resp = input("Pressione enter para ver outro cheque:")
        # Necessário pois a tela tem apenas 25 linhas
    else:
        print()
