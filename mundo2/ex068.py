# faça um programa que jogue par ou impar com computador O jogo só será interrompido quando o jogador perder
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep
print('')
print('\033[33m#\033[34m*\033[m'*25)
print('{:^50}'.format('\033[34;4mPAR ou IMPAR\033[m'))
vitorias = 0
while True:
    computador = randint(1, 10)
    jogador = (input('Digite um numero: '))
    while not jogador.isnumeric():
        jogador = (input('Digite um numero: '))
    total = computador + int(jogador)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('O que você vai jogar PAR ou IMPAR [P/I] ')).strip().upper()[0]
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if total % 2 == 0:
        resp = 'P'
    else:
        resp = 'I'
    if escolha == resp:
        print('\033[36mParabéns, você ganhou!\033[m')
        print(f'\033[34mVocê jogou {jogador} e o computador jogou {computador}\033[m')
        print('\033[34m#\033[33m*\033[m' * 25)
        print('\nVamos jogar novamente!!!')
        vitorias += 1
    else:
        print('\033[31mGame Over!\033[m')
        print(f'\033[34mVocê jogou {jogador} e o computador jogou {computador}\033[m')
        print('\033[31m#\033[33m*\033[m' * 25)
        break
print('')
print('\033[36m+ ' * 13)
print(f'+ Total de vitórias = {vitorias} +')
print('\033[36m+ \033[m' * 13)
print('FIM!!!')
