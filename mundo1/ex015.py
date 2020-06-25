#escreva um programa que pergunte a quantidade de quilometros percorridos por um carro alugado ea quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar sabendo que o carro custa 60 por dia e 0.15 por km rodado
k = float(input('Quantos quilometros rodados? '))
d = float(input('Quantos dias alugados? '))
v = (k * 0.15) + (d * 60)
print('Você alugou por {:.0f} dias, e rodou {:.1f}km\nValor de diaria R${:.2f}\nValor de quilometros rodados R${:.2f}\nValor total: R${:.2f}'.format(d, k, (d*60), (k*0.15), v))
