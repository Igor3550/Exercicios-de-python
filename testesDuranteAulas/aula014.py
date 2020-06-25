# laço de repetição while
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!')
print('PROXIMO EXEMPLO')
n1 = 1
par = impar = 0
while n1 != 0:
    n1 = int(input('Digite um valor: '))
    if n1 != 0:
        if n1 % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!!'.format(par, impar))
