#escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima da velocidade
veloc = int(input('Digite a velocidade em km/h: '))
if veloc <= 80:
    print('Você esta no limite de velocidade\nO limite é de 80km/h e sua velocidade foi {}km/h'.format(veloc))
else:
    multa = (veloc - 80) * 7
    print('Você foi multado pois excedeu o limite de velocidade de 80km/h\nSua velocidade: {}km/h\nValor da multa: R${:.2f}'.format(veloc, multa))
