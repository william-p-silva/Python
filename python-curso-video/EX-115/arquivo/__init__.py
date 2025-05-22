from funções import decoração


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('')
        decoração.cabeça('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<50}{dado[1]:>3} anos')
        print("")
        print('--' * 30)
    finally:
        a.close()

def cadastrar(nome, pessoa='desconhecido', idade=0):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        try:
            a = open(nome, 'at') # Abre o arquivo para adicionar
        except:
            print('Erro ao escrever mo arquivo!')
        else:
            a.write(f'{pessoa};{idade}\n')
            print(f'Novo registro de {pessoa} adicionado.')
        finally:
            a.close()