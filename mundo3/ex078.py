# faça um programa que leia 5 valores numericos e guarde-os em uma lista
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
lista = []
menor = maior = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        menor = maior = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        elif lista[cont] < menor:
            menor = lista[cont]
print(f'Voce digitou {lista}')
print(f'O maior valor foi {maior} e suas posições são: ', end=' ')
for co, va in enumerate(lista):
    if va == maior:
        print(co, end='... ')
print('')
print(f'O menor valor foi {menor} e suas posições são: ', end=' ')
for ca, vo in enumerate(lista):
    if vo == menor:
        print(ca, end='... ')
