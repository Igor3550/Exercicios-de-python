# faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
# Seu programa deve analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def lin():
    print('=+' * 30)


def maior(*valores):
    lin()
    m = 0
    tam = len(valores)
    print('Analisando os valores passados...')
    sleep(1)
    for v in valores:
        print(v, end=' ')
        sleep(0.5)
        if v > m:
            m = v
    sleep(0.5)
    print(f'Foram informados {tam} valores ao todo!')
    sleep(1)
    print(f'O maior valor foi {m}')


# programa principal
maior(2, 5, 8)
maior(4, 5, 1, 8, 5, 9)
maior(7, 3, 2, 4)
maior(1)
maior()
