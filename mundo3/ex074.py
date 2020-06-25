# crie um programa que vai gerar cinco números aleatorios e colocar em um tupla
# depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
nr = ()
ns = ()
maior = 0
menor = 0
maior1 = 0
menor1 = 0
for c in range(0, 5):
    nr = (randint(1, 10),)
    ns = ns + nr
    if c == 0:
        menor = (nr[0])
        maior = (nr[0])
    else:
        if (nr[0]) < menor:
            menor = (nr[0])
        elif (nr[0]) > maior:
            maior = (nr[0])
print(f'Os 5 numeros são: {ns}\nO maior foi {maior} e o menor foi {menor}')
print('OUTRO MÉTODO')
neo = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores são: {neo}')
print(f'O maior valor foi {max(neo)} e o menor foi {min(neo)}')
