def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def metade(v, f=False):
    resul = v/2
    if f:
        resul = moeda(resul)
    return resul


def aumentar(v, p, f=False):
    resul = ((v*p)/100) + v
    if f:
        resul = moeda(resul)
    return resul


def dobro(v, f=False):
    resul = v*2
    if f:
        resul = moeda(resul)
    return resul


def diminuir(v, p, f=False):
    resul = v - ((v*p)/100)
    if f:
        resul = moeda(resul)
    return resul


def resumo(v, pa, pd):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"  Preço analisado":<25} {moeda(v)}')
    print(f'{"  Dobro do preço":<25} {dobro(v, True)}')
    print(f'{"  Metade do preço":<25} {metade(v, True)}')
    print(f'{f"  {pa}% de aumento":<25} {aumentar(v, pa, True)}')
    print(f'{f"  {pd}% de deconto":<25} {diminuir(v, pd, True)}')
