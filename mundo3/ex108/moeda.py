# adapte o codigo do ex107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor
# monetario formatado

from ex107 import moeda as m


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def metade(v):
    resul = m.metade(v)
    return resul


def aumentar(v, p):
    resul = m.aumentar(v, p)
    return resul


def dobro(v):
    resul = m.dobro(v)
    return resul
