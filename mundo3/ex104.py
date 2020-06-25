# faça um programa que tenha a função leiaInt(), que vao funcionar de forma semalhante a função input() do python
# só que fazendo a validação para aceitar apenas um valor numerico
# n = leiaInt('Digite um n')


def leiaInt(txt):
    valor = 0
    while True:
        print(txt, end='')
        num = str(input())
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[1;31mERRO! Digite um numero inteiro válido!\033[m')
    return valor


# programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
