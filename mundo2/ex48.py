# faça um programa que calcule a soma entre todos os numeros impares que são multipllos de tres e que se encontram entre 1 e 500
print('A soma entre todos os numeros impares multiplos de tres entre 1 e 500: ', end='')
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(soma)
