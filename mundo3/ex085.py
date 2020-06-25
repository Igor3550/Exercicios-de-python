# faça um programa que onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica
#que mantenha separados os valores pares e impares, no final mostre os valores pares e impares em ordem crescente
lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores impares foram: {lista[1]}')
