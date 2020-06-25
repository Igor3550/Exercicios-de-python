# faça um programa que tenha uma lista chamada numeros[] e duas funções chamadas sorteia() e somaPar().
# A primeira funçao vai sortear 5 valores e vai colocalos dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função sorteia()

from time import sleep
from random import randint

numeros = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for n in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        sleep(0.5)
        numeros.append(num)
    print('PRONTO!')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}')


# programa principal
sorteia()
somaPar()
