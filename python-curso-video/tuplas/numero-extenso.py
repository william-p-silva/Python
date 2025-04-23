
extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
esc = ' '

while True:
    num = int(input("Digite um número inteiro entre 0 e 20: "))

    if num < 0 or num > 20:
        print("[ERRO] Tente Novamente. ", end='')
    if 0 <= num <= 20:
        print(f"Você digitou o número {extenso[num]}")
        while esc not in 'sn':
            esc = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
        if esc == 'n':
            break
    esc = ' '
