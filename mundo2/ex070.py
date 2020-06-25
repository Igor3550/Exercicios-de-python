# faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar
# No final, mostre:
# Qual é o total de gastos da compra
# quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato
gastos = produts = cont = pbarat = 0
nbarat = ''
while True:
    print('+ ' * 25)
    produto = str(input('Qual o nome do produto: ')).strip().title()
    while not produto.isalpha():
        produto = str(input('Qual o nome do produto: ')).strip().title()
    preco = input('Valor do produto: R$')
    while not preco.isnumeric():
        preco = input('Valor do produto: R$')
    preco = int(preco)
    gastos += preco
    cont += 1
    if preco > 1000:
        produts += 1
    if cont == 1 or preco < pbarat:
        nbarat = produto
        pbarat = preco
    continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    print('')
print('')
print('+ ' * 26)
print(f' O total de gastos foi de R${gastos:.2f}')
print(f' {produts} custam mais de R$1000.00')
print(f'{nbarat} é o produto de menor valor custando R${pbarat:.2f}')
print('+ ' * 26)
