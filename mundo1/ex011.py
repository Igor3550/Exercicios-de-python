# faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area ea quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2m².
print('\n{:*^40}\n' .format('Desafio011'))
lp = float(input('Digite a largura da parede: '))
ap = float(input('Digite a altura da parede: '))
areap = lp * ap
t = areap / 2
print('Sua parede é de {}x{}, sua area é {:.2f}m²\nVocê vai precisar {:.2f}l de tinta para pintar sua parede' .format(lp, ap, areap, t))
