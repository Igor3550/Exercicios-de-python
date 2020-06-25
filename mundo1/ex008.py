# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
print('\n{:*^40}\n'.format('Desafio008'))
n = float(input('Digite uma distancia em metros: '))
print('Metros: {:.0f}m\nCentimetros: {:.0f}cm\nMilimetros: {:.0f}mm' .format(n, n * 100, n * 1000))
