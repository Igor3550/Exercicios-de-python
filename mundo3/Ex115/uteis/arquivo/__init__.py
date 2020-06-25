from Ex115.uteis.interface import *


def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {txt} criado com sucesso')


def lerArquivo(txt):
    cabecalho('PESSOAS CADASTRADAS')
    try:
        a = open(txt, 'rt')
    except:
        print('Ocorreu um Erro!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(F'{dado[0]:<40}{dado[1]} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ouve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ouve um erro ao tentar escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
