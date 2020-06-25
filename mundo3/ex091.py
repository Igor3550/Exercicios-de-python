# faça um programa onde quatro jogadores jogam um dado e tenham ressultados aletorios.
# Guarde esses resultados em um dicionario.
# No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter
menu = int(input('0 para Versão minha 1 para Guanabara: '))
if menu == 0:
    valores = []
    jogadores = dict()
    print('+ ' * 15)
    print(f'{"JOGO DE DADOS": ^30}')
    print()
    for j in range(0, 4):
        cont = 0
        n = randint(1, 6)
        print(f'Jogador {j}: {n}')
        sleep(1)
        if j == 0:
            valores.append((j, n))
        else:
            for v in valores:
                if n <= v[1]:
                    cont += 1
            if cont == 0:
                valores.insert(0, (j, n))
            else:
                valores.insert(cont, (j, n))
    print()
    print('+ ' * 15)
    print(f'{"RESULTADO":^30}')
    sleep(1)
    for c in range(0, 4):
        jogadores[c] = valores[c]
    for k in jogadores.items():
        print(f'{k[0]+1}°Lugar Jogador {k[1][0]}: {k[1][1]}')
        sleep(1)
else:
    # VERSÃO GUANABARA>
    print('===VERSÃO GUANABARA===')
    print()
    ranking = list()
    jogo = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)}
    print('Valores sorteados')
    for k, v in jogo.items():
        print(f'{k} jogou {v}')
        sleep(1)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    print('Ranking dos jogadores')
    for i, v in enumerate(ranking):
        print(f'{i+1}° lugar: {v[0]} com {v[1]}')
