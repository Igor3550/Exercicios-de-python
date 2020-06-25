# faça um programa que ajude um jogador da megasena a criar palpites.
# o programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60
# para cada jogo cadastrando tudo em uma lista
from time import sleep
from random import randint
jogos = []
print(f'{" MegaSena ":+^45}')
print()
jogs = int(input('Quantos jogos voce deseja que eu sorteie? '))
print()
for i in range(0, jogs):
    for c in range(0, 6):
        n = randint(1, 60)
        for n in jogos:
            n = randint(1, 60)
        jogos.append(n)
    jogos.sort()
    sleep(1)
    print(f'Jogo {i+1}: {jogos}')
    jogos.clear()
print()
print(f'{" Boa sorte ":+^35}')
