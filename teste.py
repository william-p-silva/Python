def helloWord(f):
    print(f)
    
    for k, v in enumerate(f):
        print(f"{v}", end='')


dic = {'nome': "william", "idade": [12, 25, 65, 19]}


helloWord(f"{dic}")
helloWord("Ola a todos meus caros compatriotas de guerra")
helloWord("O Capitão PT é um otimo personagem")
