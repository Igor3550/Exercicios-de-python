#secreva um programa que faça o computador escolher um numero entre 0 e 5 e peça para que o usuário tente descobrir qual foi o numero escolhido.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
lista = [1, 2, 3, 4, 5]
num = random.choice(lista)
print('{:*^40}'.format(' Jogo de adivinhação '))
print('Vamos jogar!')
escolha = int(input('Pensei em um numero de 0 a 5, adivinhe qual é: '))
print('PROCESSANDO...')
sleep(2)
if escolha == num:
    print('Parabens você escolheu o numero que eu pensei! Numero {}'.format(num))
else:
    print('Ahhh')
    print('Desculpe você escolheu {} e eu pensei {}'.format(escolha, num))
