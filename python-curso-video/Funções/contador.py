
from time import sleep
def contador(i, f, p):
    if i < f:
        if p < 0:
            p = p * -1
        print(f'Contando de {i} até {f} de {p} em {p}...')
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)#o flush=True faz com que o print seja executado com o sleep em cada loop sem ele a tela congela por um tempo e aparece tudo de uma vez
            sleep(0.5)
        
    else:
        
        if p > 0:
            p = -p
        print(f'Contando de {i} até {f} de {p} em {p}...')
        for c in range(i, f, p):
            print(c, end=' ', flush=True)#o flush=True faz com que o print seja executado com o sleep em cada loop sem ele a tela congela por um tempo e aparece tudo de uma vez
            sleep(0.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, -1)
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
if passo == 0:
    passo = 1
contador(ini, fim, passo)