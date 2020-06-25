# faça um programa que leia dois valores e mostre um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
menu = 0
resultado = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
while menu != 5:
    if menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    print('''
              MENU
    ************************
    *[1] Somar             *
    *[2] Multiplicar       *
    *[3] Maior             *
    *[4] Novos Numeros     *
    *[5] Sair do programa  *
    ************************''')
    menu = int(input('\nO que deseja fazer? '))
    if menu == 1:
        resultado = n1 + n2
        print('O resultado de {} + {}: {}\n'.format(n1, n2, resultado))
    elif menu == 2:
        resultado = n1 * n2
        print('O resultado {} x {}: {}\n'.format(n1, n2, resultado))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}\n'.format(n1, n2, maior))
print('FIM!')
