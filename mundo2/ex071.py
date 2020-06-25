# faça um programa que simule o funcionamento de um caixa eletronico
# No inicio pergunte ao usuario qual será o valor a ser sacado (numero iteiro) e o programa va infomar quantas cédulas de cada valor serão entregues
# Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1

valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
c = v = d = u = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} notas de R${ced:.2f}')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break
