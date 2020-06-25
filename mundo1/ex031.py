# faça um programa que pergunte a distancia de uma viagem em km
# Calcule o preço da passagem, cobrado R$0.50 por km para viagens de ate 200km
# E R$0.45 para viagens mais longas
dist = int(input('Digite a distancia da viagen em km: '))
if dist <= 200:
    preco = dist * 0.5
    print('O valor de sua passagem será de R${:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('O valor da passagem será de R${}'.format(preco))
