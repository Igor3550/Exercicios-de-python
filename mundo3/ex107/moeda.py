# crie um modulo moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# faça tmb um programa que importe esse modulo e use algumas dessas funções


def aumentar(v, p):
    res = v + (p*v)/100
    return res


def diminuir(v, p):
    res = v - (p*v)/100
    return res


def metade(v):
    res = v/2
    return res


def dobro(v):
    res = v*2
    return res
