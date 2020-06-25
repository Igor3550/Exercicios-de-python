# faça um programa que refaça o 051 lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
#decimo = n + (10 - 1) * r
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = 0
while decimo != 10:
    print(n, end=' ')
    n = n + r
    decimo += 1
