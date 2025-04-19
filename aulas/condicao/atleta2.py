idade_atleta = int(input('Qual sua idade? '))

if idade_atleta >= 18 and idade_atleta <= 35:
    con_fisico = input('Seu condicionamento físico é adequado? ')
    
    if con_fisico == 'não':
        permissão_med = input('vc tem permissão medica? ')
    if con_fisico == 'sim' or permissão_med == 'sim':
        print('Vc foi inscrito. Parabéns!! ')
    else: 
        print('Vc não pode ser inscrito ')
else:
    print('Vc não pode ser inscrito :( ')