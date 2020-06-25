# faça um programa que leia oo ano de nascimento de sete pessoas. no final mostre quantas pessoas aindda não atingiram a maioridade e quantas ja são maiores
from datetime import  datetime
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if datetime.today().year - ano >= 21:
        maior += 1
    else:
        menor +=1
print('{} pessoas já são maiores de idade'.format(maior))
print('{} pessoas ainda não atingiram a maioridade'.format(menor))
