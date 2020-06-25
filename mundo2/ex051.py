# faça um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa progressão
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos dessa PA são: ')
decimo = n + (10 - 1) * r
for c in range(n, decimo+r, r):
    print(c, end=', ')
