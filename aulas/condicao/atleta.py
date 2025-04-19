idade_atleta = int(input('Qual sua idade? '))
cond_fisico = input('Seu condicionamento físico é adequado? ')
permissão_med = input('Você tem permissão medica? ')

if idade_atleta >= 18 and idade_atleta <= 35 and (cond_fisico == 'sim' or permissão_med == 'sim'): 
    print("parabés você foi inscrito na competição")
else:
    print('Você não pode ser inscrito')