# crie um programa que tenha uma função fatorial que receba dois paramentros:
# o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico (opcional)
# indicando se sera mostrado ou nao na tela o processo de cálculo fatorial


def fatorial(n, show=False):
    """
    => Calcula o fatorial de numero
    :param n: numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: retorna o fatorial de um numero n
    """
    f = 1
    print()
    print('-' * 40)
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
    return f


# programa principal
print(fatorial(5, show=True))
print()
help(fatorial)
