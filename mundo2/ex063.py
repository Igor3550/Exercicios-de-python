# faça um programa que leia um numero n qualquer e mostre na tela os n primeiros elementos ded uma sequencia de fibonancci
# ex:7 = 0 1 1 2 3 5 8
n = int(input('Digite um numero: '))
c = 0
b = 1
r = 0
a = 0
while c < n:
    print(r)
    a = r
    r += b
    b = a
    c += 1
