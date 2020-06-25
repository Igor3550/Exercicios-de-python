# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
'''from math import ceil, modf, trunc
num = float(input('Digite um numero real: '))
n = trunc(num)
print('A porção inteira de {} é equivalente a {}'.format(num, n))'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} sua parte inteira é {}'.format(num, int(num)))
