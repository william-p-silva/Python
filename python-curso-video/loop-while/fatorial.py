num = int(input("Digite um número: "))
f = 1
c = num
for n in range(1, c +1):
    if c > 1:
        print(f" {c} X ", end='')
    else:
        print(f" {c} = ", end='')
    f *= c
    c -= 1
print(f)
