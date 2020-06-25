#faça um programa que melhore o jogo 028 onde o computador vai pensar em um numero de 0 a 10
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint
from time import sleep
num = randint(0, 10)
print('{:*^40}'.format(' Jogo de adivinhação '))
print('Vamos jogar!')
escolha = int(input('Pensei em um numero de 0 a 10 tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
tentativa = 1
while escolha != num:
    tentativa += 1
    print('\033[31mVocê errou!!\033[m')
    if escolha > num:
        print('Menos...')
    elif escolha < num:
        print('Mais...')
    escolha = int(input('\n\033[mTente novamente: '))
print('\033[36mParabéns você acertou! \n\033[mEu pensei no numero {} e você conseguiu acertar em {} tentativas!'.format(num, tentativa))
