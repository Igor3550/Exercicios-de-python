# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 a 0, com uma pausa de 1s entre eles
from time import sleep
import emoji
print('A contagem regressiva para o estouro de fogos vai começar!!!')
sleep(1)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':boom::tada::boom::tada:', use_aliases=True))
