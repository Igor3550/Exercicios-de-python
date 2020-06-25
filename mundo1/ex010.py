# faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar conssidere US$: R$ 3.27
print('\n{:*^40}\n' .format('Desafio010'))
din = float(input('Quanto dinheiro você tem na carteira? R$'))
do = din / 3.27
print('Você tem R${:.2f} e pode comprar US${:.2f}' .format(din, do))
