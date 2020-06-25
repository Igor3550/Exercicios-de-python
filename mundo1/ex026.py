#faça um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
#Em que posição ela aparece pela ultima vez
frase = input('Digite uma frase: ')
frase = frase.upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('Primeiro a letra "A" aparece na posição {}'.format(frase.find('A') + 1))
print('A ultima vez ela aparece na {}ª posição'.format(frase.rfind('A') + 1))
