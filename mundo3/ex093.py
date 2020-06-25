# faça um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final tudi isso será guardado em um dicionario,
# incluindo o total de gols feitos durante o campeonato
jogador = dict()
gols = list()
jogador['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantos partidas {jogador["jogador"]} jogou: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('+ ' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
print('+ ' * 20)
print(f'O jogador {jogador["jogador"]} jogou {len(gols)} partidas')
for c, g in enumerate(gols):
    print(f'{"=>":>6} Na partida {c} fez {g} gols')
print(f'Com um total de {jogador["total"]} gols')
print('+ ' * 20)
