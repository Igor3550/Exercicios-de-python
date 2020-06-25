# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot, sqrt
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
h = hypot(x, y)
print('o comprimento da hipotenusa é de {:.2f}'.format(h))
