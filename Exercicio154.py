NUM = []
# Trecho de entrada de 15 elementos
for L in range(15):
    num = int(input(f"Digite o {L + 1}º número: "))
    NUM.append(num)

# Trecho de saída
print("\nRELACAO DOS NUMEROS\n")
for L in range(15):
    print(f"{L + 1} - {NUM[L]}", end=' ')
    if NUM[L] % 2 == 0:
        print("é PAR")
    else:
        print("é IMPAR")
