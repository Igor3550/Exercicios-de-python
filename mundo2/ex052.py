#faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
n = int(input('Digite um numero inteiro: '))
primo = 0
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        primo += 1
    else:
        print('\033[33m', end=' ')
    print(c, end=' ')
if primo == 2:
    print('\n \033[36mO numero {} é um numero PRIMO'.format(n))
else:
    print('\n\033[31mO numero {} NÃO é um numero PRIMO'.format(n))
