import moeda.conversor
from dados import dado
#from moeda import conversor
while True:
    num = dado.lerDinheiro("Digite um preço: R$ ")
    moeda.conversor.tudo(num, 10, 40, True)
    #num, percentagem de aumento, porcentagem de desconto