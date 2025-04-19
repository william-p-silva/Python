

i = int(input("Onde vai começar? "))
f = int(input("Onde vai terminar? "))
r = int(input("Qual a razão? "))

decimo = i + (10 - 1) * r
if i < f:
    for c in range(i, f+1, r):
        print(c, end="  ")
elif i > f:
    for c in range(i, f-1, -r):
        print(c, end="  ")
print("\n")
for c in range(i, decimo + r, r):

        print( c, end="  ")