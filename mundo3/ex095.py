# Aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador

from time import sleep
jogadores = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador['jogador'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantos partidas {jogador["jogador"]} jogou: '))
    total = 0
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
        total += gols[c]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N] '))
        if resp in 'SsNn':
            break
        print('Erro! Digite apenas S ou N')
    if resp in 'Nn':
        break
print('+ ' * 25)
print(f'{"Cod."} {"Nome":10} {"Gols":20} {"Total"}')
cod = 0
for j in jogadores:
    nome = j['jogador']
    tot = j['total']
    print(f'{cod:<5}{nome}{" " * (12-len(nome))}{j["gols"]}{" " * (21-(len(j["gols"])*3))}{tot}')
    cod += 1
print('+ ' * 25)
print()
while True:
    esc = int(input('Deseja ver o aproveitamento de qual jogador: (999 para sair) '))
    if esc == 999:
        print(' <<ENCERRANDO', end='')
        sleep(1)
        print('>', end='')
        sleep(1)
        print('>', end='')
        break
    else:
        print('+ ' * 25)
        if esc >= cod:
            print('{}Desculpe! Cod. não encontrado. Tente Novamente!{}'.format('\033[31m', '\033[m'))
            print('+ ' * 25)
        else:
            print(f'{"<<-- LEVANTAMENTO DO JOGADOR"} {jogadores[esc]["jogador"]} -->>')
            for p, g in enumerate(jogadores[esc]['gols']):
                sleep(1)
                print(f' ==> Na partida {p} fez {g} gols!')
            print('+ ' * 25)
