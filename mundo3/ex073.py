# crie uma tupla peenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação depois mostre:
# Apenas os 5 primeiros colocados
# os ultimos 4 colocados da tabela
# uma lista com os times em ordem alfabetica
# Em que posição na tabela está o time da chapecoense

times = ('São Paulo', 'Santos', 'Cruzeiro', 'Flamengo', 'Corinthians', 'Internacional', 'Gremio', 'Flumense',
         'Atlético-MG', 'Palmeiras', 'Athletico Paranaense', 'Botafogo', 'Vasco', 'Goiás', 'Coritiba', 'Figueirense',
         'Vitória', 'Ponte Preta', 'Sport', 'Bahia')
print(f'O top 20 brasileirão: \n{times}')
print('')
print('Os 5 primeiros são:')
for c in range(0, 5):
    print(f'{c+1}°{times[c]}', end='  ')
print('')
print('')
print(f'Os quatro últimos times são: {times[-4:]}')
print('')
print(f'Times em ordem alfabetica: {sorted(times)}')
print('')
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição')
