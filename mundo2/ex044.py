# faça programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
# a vista dinheiro/cheque 10% de desconto
# a vista no cartão de 5% de desconto
# em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

preco = float(input('Qual o valor do produto? R$'))
print('+ '*17)
print('+ Qual a forma de pagamento?    +\n+ 1- A vista(Dinheiro / Cheque) +\n+ 2- a vista no Cartão          +\n+ 3- Em até 2x no cartão        +\n+ 4- 3x ou mais no cartão       +')
print('+ '*17)
forma = int(input('Forma de pagamento: '))
desc1 = preco - (preco * 10 / 100)
desc2 = preco - (preco * 5 / 100)
juros = preco + (preco * 20 / 100)
if forma == 1:
    preco = desc1
elif forma == 2:
    preco = desc2
elif forma == 4:
    preco = juros
print('O valor total do produto a ser pago: R${:.2f}'.format(preco))
