# crie um algoritmo que leia um numero e mostre o seu dobro, triplo, e sua raiz quadrada
print('{:*^40}' .format('Desafio006'))
n = float(input('Digite um numero: '))
d = 2 * n
t = n * 3
rd = n ** (1/2)
print('O dobro de {} é {}\nO triplo é {}\nA raiz quadrada é {}' .format(n, d, t, rd))
