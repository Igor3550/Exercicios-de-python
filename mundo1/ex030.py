# faça um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
n = int(input('Digite um numero:'))
if n % 2 == 0:
    print('O numero {} é Par'.format(n))
else:
    print('O numero {} é Impar'.format(n))
