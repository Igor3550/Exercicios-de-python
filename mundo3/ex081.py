# faça um programa que leia varios valores e coloque em uma lista depois disso mostre
# quantos numeros foram digitados
# a lista de valores ordenada de forma decrescente
# se o valor 5 foi digitado e esta ou não na lista

from time import sleep
valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar: [S/N] ')).upper().strip()
    if cont == 'N':
        break
print(f'Analizando a lista: {valores}')
sleep(0.5)
for c in range(0, 5):
    print('.', end='')
    sleep(1)
print('')
print('+ ' * 25)
print(f'Voce digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {valores}')
if 5 in valores:
    print(f'O valor 5 esta na lista e esta na {valores.index(5)} posição!')
else:
    print('O valor 5 não esta na lista!')
