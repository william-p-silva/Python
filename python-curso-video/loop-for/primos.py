

num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" " )
        total += 1
    else:
        print("\033[31m", end=" ")
    print(c, end='')
if total == 2:
    print("\n\033[mNúmero primo")
else:
    print("\n\033[mnúmero comun")