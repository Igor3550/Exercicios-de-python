# melhore o desafio 061, perguntando quantos termos a mais ele vai mostrar,
# o programa encerra quando ele disser que quer mostrar 0 termos.
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
ultimo = 0
termo = 10
while termo != 0:
    print(n, end=' ')
    n = n + r
    if termo == ultimo+1:
        termo = int(input('\nQuantos termos você quer mostrar? '))
    else:
        termo -= 1
print('FIM!!')
