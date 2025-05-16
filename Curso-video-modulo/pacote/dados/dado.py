def lerDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada == '' or len(entrada) == 0:
            print(f"ERRO: '{entrada}' é um preço inválido!")
        else:
            valido = True
            entrada = entrada.replace(',', '.')
    return float(entrada)