def valida(txt):
    while True:
        try:
            esc = int(input(txt))
        except ValueError:
            print('\033[31mErro: por favor digite um numero inteiro válido\033[m')
        else:
            break
    return esc


def linha(tam=50):
    return '-' * tam


def cabecalho(txt):
    t = len(linha())
    print(linha())
    print(txt.center(t))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    esc = valida('\033[36mSua Opção: \033[m')
    return esc
