# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente
import math
a = int(input('Digite um angulo: '))
s = math.cos(math.radians(a))
c = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print('O angulo de {}° tem seno {:.2f}°\nCosseno {:.2f}°\nTangente {:.2f}°'.format(a, s, c, t))
