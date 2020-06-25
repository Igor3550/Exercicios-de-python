# faç um programa que uma função chamada área(), que receba as dimmensões de um terreno retangular (largura) e
# (comprimento) e mostre a area do terreno


def area(larg, comp):
    a = (comp * larg)
    print(f'A área de um terreno de {larg}x{comp} é de: {a}m²')


# programa principal
l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
area(l, c)
