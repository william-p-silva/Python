ex = input("Digite um número: ")
pilha = []

for s in ex:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Correto")
else:
    print("Incorreto")