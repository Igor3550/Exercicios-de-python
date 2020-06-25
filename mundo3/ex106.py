# faça um mini sistema que utilize o iteractive Help de python. O usuario vai digitar o comando e o manual vai aparecer
# Quando o usuario digitar a palavra "FIM", o programa vai encerrar OBS: Use cores

from time import sleep


def cores(cor=''):
    cod = ''
    if cor == 'resul':
        cod = '\033[1;7;30m'
    elif cor == 'acces':
        cod = '\033[1;30;44m'
    elif cor == 'tit':
        cod = '\033[1;30;43m'
    elif cor == 'fim':
        cod = '\033[1;30;41m'
    elif cor == '':
        cod = '\033[m'
    elif cor == 'load':
        cod = '\033[46m \033[m'
    else:
        cod = '\033[m'
    return cod


def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


def loading():
    print(cores(), end='')
    for c in range(0, 201):
        print(cores('load'), end='')
        sleep(0.01)
    print(cores())


def PyHelp():
    while True:
        print(cores(), end='')
        print(cores('tit'), end='')
        escreva('SISTEMA DE AJUDA PyHELP')
        print(cores(), end='')
        com = input('Função ou Biblioteca > ')
        if com.upper() != 'FIM':
            print(cores("acces"), end='')
            escreva(f'Acessando manual do comando "{com}"')
            loading()
            print(cores(), end='')
            print(cores("resul"), end='')
            help(com)
        else:
            print(cores(), end='')
            print(cores('fim'), end='')
            escreva('Finalizando! Até logo')
            break


# programa principal
escreva('Loading modules')
loading()
PyHelp()
