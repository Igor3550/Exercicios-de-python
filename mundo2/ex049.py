# faça um programa que mostre a tabuada de um numero refaça o ex009
n = int(input('Digite um numero pra ver a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
