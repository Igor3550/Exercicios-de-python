cores = ['\033[1:7:34:40m',  # azul
         '\033[1:7:33:40m',  # amarelo
         '\033[m']


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
    print(f'{cores[0]}-{cores[2]}' * 40)
    print(f'{cores[0]}{"RESUMO DO VALOR":^40}{cores[2]}')
    print(f'{cores[0]}-{cores[2]}' * 40)
    print(f'{cores[1]}{"  Preço analisado":<25} {moeda(v)}{" " * (14-(len(moeda(v))))}{cores[2]}')
    print(f'{cores[1]}{"  Dobro do preço":<25} {moeda(dobro(v))}{" " * (14-(len(moeda(dobro(v)))))}{cores[2]}')
    print(f'{cores[1]}{"  Metade do preço":<25} {moeda(metade(v))}{" " * (14-(len(moeda(metade(v)))))}{cores[2]}')
    print(f'{cores[1]}{f"  {pa}% de aumento":<25} {moeda(aumentar(v, pa))}{" " * (14-(len(moeda(aumentar(v, pa)))))}{cores[2]}')
    print(f'{cores[1]}{f"  {pd}% de deconto":<25} {moeda(diminuir(v, pd))}{" " * (14-(len(moeda(diminuir(v, pd)))))}{cores[2]}')
