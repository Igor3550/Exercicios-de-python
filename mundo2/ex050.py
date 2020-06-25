#faça um programa que leia seis numeros e mmostre a soma apenas daqueles que forem pares, se for impar ele vai ser desconsiderado
soma = 0
for c in range(0, 6):
    if c > 0:
        n = int(input('Digite outro numero: '))
        if n % 2 == 0:
            soma += n
    else:
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            soma += n
print('A soma de todos os numeros pares é: {}'.format(soma))
