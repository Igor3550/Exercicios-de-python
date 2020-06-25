# faça um programa que vai ler vários valores e colocar em uma lista
# depois disso crie duas çistas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente
# ao final mostre o conteudo das tres listas geradas
normal = []
par = []
impar = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    normal.append(num)
    conti = ' '
    cont += 1
    while conti not in 'SN':
        conti = str(input('Deseja continuar: [S/N] ')).strip().upper()
    if conti == 'N':
        break
for c in normal:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Voce digitou {cont} valores')
print(f'Lista normal: {normal}')
print(f'Lista com valores pares: {par}')
print(f'Lista com valores impares: {impar}')
