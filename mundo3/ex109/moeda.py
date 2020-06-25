from ex107 import moeda as m7


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def metade(v, f=False):
    resul = m7.metade(v)
    if f:
        resul = moeda(resul)
    return resul


def aumentar(v, p, f=False):
    resul = m7.aumentar(v, p)
    if f:
        resul = moeda(resul)
    return resul


def dobro(v, f=False):
    resul = m7.dobro(v)
    if f:
        resul = moeda(resul)
    return resul


def diminuir(v, p, f=False):
    resul = m7.diminuir(v, p)
    if f:
        resul = moeda(resul)
    return resul
