#faça um programa que leia varios nome e peso de vários pessoas guardando tudo em uma lista
# no final mostre:
# quantas pessoas foram cadastradas
# uma listagem com sd pessoas mais pesadas
# uma listagem com as pessoas mais leves
lista = []
pessoas = list()
cont = maior = menor = 0
nmaior = []
nmenor = []
while True:
    pessoas.append(str(input('Qual o nome: ')))
    pessoas.append(int(input('Qual o peso: ')))
    lista.append(pessoas[:])
    pessoas.clear()
    cont += 1
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
for p in lista:
    if p == lista[0]:
        menor = maior = p[1]
        nmaior.append(p[0])
        nmenor.append(p[0])
    else:
        if p[1] > maior:
            nmaior.clear()
            nmaior.insert(0, p[0])
            maior = p[1]
        elif p[1] < menor:
            nmenor.clear()
            nmenor.insert(0, p[0])
            menor = p[1]
        elif p[1] == maior:
            nmaior.append(p[0])
        elif p[1] == menor:
            nmenor.append(p[0])
print(f'Voce cadastrou {cont} pessoas')
if len(nmaior) >= 2:
    print(f'O maior peso foi de {maior:.1f}kg, peso de {nmaior[0]} e {nmaior[1]}')
elif len(nmaior) == 1:
    print(f'O maior peso foi de {maior:.1f}kg, peso de {nmaior[0]}')
if len(nmenor) >= 2:
    print(f'O maior peso foi de {menor:.1f}kg, peso de {nmenor[0]} e {nmenor[1]}')
elif len(nmenor) == 1:
    print(f'O maior peso foi de {menor:.1f}kg, peso de {nmenor[0]}')
