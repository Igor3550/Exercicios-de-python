# desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r2 + r3) >= r1 and (r1 + r2) >= r3 and (r3 + r1) >= r2:
    print('As tres retas formam um triangulo')
else:
    print('As tres retas não formam um triangulo')
