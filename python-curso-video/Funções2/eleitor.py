from datetime import date

def voto(anoNascimento):
    """
    Função para verificar se a pessoa pode votar ou não.
    :param anoNascimento: ano de nascimento da pessoa
    :return: retorna uma string com a situação do voto
    """
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
       return f"voê ainda não pode Votar, você tem {idade} anos"
    elif 16 <= idade < 18 or idade > 65:
       return f"Seu voto é opcional, você tem {idade} anos"
    elif 18 <= idade < 65:
       return f"Seu voto é obrigatório, você tem {idade} anos"

Nascimento = int(input("Digite o ano de nascimento: "))
print(voto(Nascimento))