# faça um programa que que o usuario pode digitar vários valores numericos e cadastre-os em uma lista.
# Caso o numero já estiver lá dentro ele não sera adicionado
# No final serão exibidos em ordem crescente
valores = []
conti = cont = 0
while True:
    conti += 1
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Valor não adicionado!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar :[S/N] ')).upper().strip()
    if continuar == 'N':
        break
valores.sort()
print(f'Voce digitou {cont} valores: {valores}')
