#Faça um programa que leia o preço de um produto e mostre seu novo preço cocm 5% de desconto
print('\n{:*^40}\n' .format(' Desafio012 '))
pa = float(input('Digite o valor do produto: '))
d = (pa * 5) / 100
pd = pa - d
print('Preço normal: R$ {:.2f}\nPreço com 5% de desconto: R$ {:.2f}' .format(pa, pd))
