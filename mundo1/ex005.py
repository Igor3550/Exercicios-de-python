# faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessoe
print('\n{:*^40}'.format('Desafio005'))
n = int(input('Digite um valor: '))
print('O sucessor de {} é {}, e o antecessor é {}' .format(n, (n+1), (n-1)))
