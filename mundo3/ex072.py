# faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
# seu porgrama deverá ler um numero pelo teclado (entre e 20) e  mostra-lo por extenso

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)

n = int(input('Digite um numero entre 0 e 20: '))

while True:
    if (n >= 0) and (n <= 20):
        print(f'{n} por extenso é: {extenso[n]}')
        break
    else:
        n = int(input('Tente novamente, Digite um numero entre 0 e 20: '))
print('FIM!')
