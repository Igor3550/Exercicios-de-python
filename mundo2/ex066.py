# crie um programa que leia vários numeros inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999
# No final mostre quantos números foram digitados e qual foi a soma entre eles
soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para terminar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} e a soma entre eles foi {soma}')
