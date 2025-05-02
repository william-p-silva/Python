from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
for c in range(1,5):
    jogadores[f"jogador{c}"] = randint(1,6)

for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado")
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#As duas linhas acima vão ordernar o dicionário em ordem decrescente. É recomendado criar um lista para isso. Temos que importar a biblioteca operator e usar o comando itemgetter
print()
print("-="*30)
for i, v in enumerate(ranking):
     sleep(1)
     print(f"{i+1}º -- {v[0]} tirou {v[1]} no dado")
     
     