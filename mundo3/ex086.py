# faça um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# no final moistre a matriz na tela com a formatação correta
matriz = [[[], [], []], [[], [], []], [[], [], []]]
for c in range(0, 3):
    for v in range(0, 3):
        num = int(input(f'Digite um valor para a posição ({c}, {v}): '))
        matriz[c][v].append(num)
print('+ ' * 25)
print('Sua matriz 3x3 ficou assim: ')
for a in matriz:
    for i in a:
        print(f'[{i[0]:^5}]', end=' ')
    print()
