# aprimore o ex086 mostrand o no fiinal
# a soma de todos os valores pares digitados
# a soma dos valores da terceira coluna
# o maior valor da segunda linha
from time import sleep
matriz = [[[], [], []], [[], [], []], [[], [], []]]
somapares = somaterc = maior = lin = 0
for c in range(0, 3):
    for v in range(0, 3):
        num = int(input(f'Digite um valor para a posição ({c}, {v}): '))
        matriz[c][v].append(num)

print('+ ' * 25)
print('Sua matriz 3x3 ficou assim: ')

for a in matriz:
    cont = 0
    lin += 1
    for i in a:
        cont += 1
        print(f'[{i[0]:^5}]', end=' ')
        if i[0] % 2 == 0:
            somapares += i[0]
        if cont == 3:
            somaterc += i[0]
        if lin == 2:
            if i[0] > maior:
                maior = i[0]
    print()
print()
print('Analisando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print()
print(f'A soma de todos os valores pares foi: {somapares}')
print(f'A soma dos valores na terceira coluna foi: {somaterc}')
print(f'O maior valor da segunda linha é: {maior}')
