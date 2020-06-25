# faça um programa que tenha uma funçao chamada contador(), que receba tres parametros inicio, fim e passo e realize
# a contagem: Seu programa deve realiza tres contagens atraves da função criada:
# A De 1 a 10 de 1 em 1
# b dE 10 A 0, DE 2 EM 2
# C Uma contagem personalizada

from time import sleep


def lin():
    print('=+' * 20)


def contador(inicio, fim, passo):
    lin()
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            cont += passo
            sleep(0.3)
        print('FIM!')
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print()
print('Agora é sua vez de personalizar a contagem!')
while True:
    ini = int(input('Inicio: '))
    fi = int(input('Fim: '))
    pas = int(input('Passo: '))
    contador(ini, fi, pas)
    resp = str(input('Deseja comtinuar: [S/N] '))
    if resp in 'Nn':
        break
