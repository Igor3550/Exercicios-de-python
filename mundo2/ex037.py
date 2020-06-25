# faça um programa que leia um numero inteiro qualquer e peça para o usuário escolher a base de conversão
# 1 para binario 2 para octal 3 para hexadecimal
n = int(input('Digite um numero: '))
esc = int(input('''Escolha a base de conversao:
1- Para Binario
2- Para Octal
3- Para Hexadecimal
Escolha: '''))
if esc == 1:
    print('{} convertido para BINARIO é {}'.format(n, bin(n)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente!')
