a = [0] * 10

for L in range(10):
    print(f"Elemento do vetor a[{L}]: ", end="")
    n = int(input())
    c = 0
    while n <= a[c]:
        c += 1

    if L > 0:
        for d in range(L, c, -1):
            a[d] = a[d - 1]
    
    a[c] = n

print("\nVetor Ordenado\n")
for L in range(10):
    print(f"a[{L + 1}] - {a[L]}")

print()
