# faça um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre
# quantas vezes apareceu o valor 9
# em que posição foi gigitado o primeiro valor 3
# quais foram os números pares
from time import sleep
resul = par = ()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))
lista = (n1, n2, n3, n4)
for c in lista:
    if c % 2 == 0:
        resul = (c,)
        par += resul
print(f'Os valores são: {lista}')
print('Analisando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
if lista.count(9) != 0:
    if lista.count(9) == 1:
        print(f'O valor "9" apareceu {lista.count(9)} vez')
    else:
        print(f'O valor "9" apareceu {lista.count(9)} vezes')
else:
    print('O valor "9" não foi digitado!')
if lista.index(3) != ():
    print(f'O primeiro "3" foi digitado na {lista.index(3)+1}ª posição')
else:
    print('O valor "3" não foi digitado!')
if par == ():
    print('Não ouve valor "PAR" digitado!')
else:
    for pos, cont in enumerate(par):
        if pos == 0:
            print(f'Os valores pares foram: {cont}', end=' ')
        else:
            print(cont, end=' ')
print('\nFIM!!!')
