# 'idadeEleitoral' é um parâmetro (valor que a função recebe)
def verificarCondicaoEleitoral(idadeEleitoral):
    # a função executa um bloco de código quando é chamada
    if idadeEleitoral < 16:
        return "Você não pode votar"

    elif 16 <= idadeEleitoral <= 18 or idadeEleitoral > 70:
        return "Seu voto é facultativo"

    else:
        return "Seu voto é obrigatório"



# ---------------------------
# Chamada de função
# ---------------------------

idade = 16  # variável que armazena um valor

# ao chamar a função, passamos 'idade' como argumento
# esse valor é enviado para o parâmetro 'idadeEleitoral'
print(verificarCondicaoEleitoral(idade))