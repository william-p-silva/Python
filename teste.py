def helloWord(f):
    print(f)
    print(type(f))
    for k, v in enumerate(f):
        print(f"{v}", end='')


dic = {'nome': "william", "idade": [12, 25, 65, 19]}


helloWord(f"{dic}")

