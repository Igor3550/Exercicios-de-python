# faça um programa que o usuario possa digitar 5 varios valores e cadastre-os em uma lista
# lá na posição correta de inserção sem usar o sort() no final mostre a lista ordenada
lista = []
for cont in range(0, 5):
    maior = 0
    num = ' '
    while not num.isnumeric():
        num = (input('Digite um valor: '))
    num = int(num)
    if cont == 0:
        lista.append(num)
        print('Adicionado no final da lista')
    else:
        for v, c in enumerate(lista):
            if num > c:
                maior += 1
        if maior == 0:
            lista.insert(0, num)
            print('Adicionado na posição 0!')
        else:
            lista.insert(maior, num)
            if maior > v:
                print('Adicionado no final da lista!')
            else:
                print(f'Adicionado na posição {maior}')
print(f'A lista em ordem crescente fica {lista}')
