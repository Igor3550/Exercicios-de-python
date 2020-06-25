# faça um programa que que leia um numero e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1= 120
n = int(input('Digite um valor para ver seu fatorial: '))
resul = 1
print('Resultado {}!:'.format(n))
while n > 0:
    if n > 1:
        print('{} x'.format(n), end=' ')
        resul *= n
        n -= 1
    else:
        print('{}= {}'.format(n, resul))
        resul *= n
        n -= 1
