# faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# para menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
