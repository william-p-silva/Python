def linha(tam=30):
    print("--" * tam)


def cabeça(msg):
    linha()
    print(f"{msg:^60}")
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f"Opção {c} - {item} ")
        c += 1
    linha()


def decEscolha(n):
    linha()
    print(f"{"Opção":>31} {n}")
    linha()