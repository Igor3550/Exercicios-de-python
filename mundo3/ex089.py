# crie um programa que leia o nome e duas notas de vários alunos e guarde em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

lista = list()
alunos = list()
alun = 0
while True:
    alunos.append(str(input('Nome: ')).strip().title())
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    lista.append(alunos[:])
    alunos.clear()
    alun += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
con = 0
print('+ '*12)
print(f'{" BOLETIM ":^20}')
print(f'{"N°.":<5}{"Nome":10}{"Média"}')
for a in lista:
    con += 1
    cont = media = s = 0
    for n in a:
        cont += 1
        if cont == 1:
            print(f'{con-1:<4}', end=' ')
            print(f'{n:10}', end=' ')
        if cont > 1:
            s += n
        if cont == 3:
            media = s/2
            print(media, end=' ')
    print()
print('+ '*12)
while True:
    nota = int(input('Qual aluno voce quer ver as notas? (999 para sair): '))
    print()
    if nota == 999:
        break
    if nota >= alun:
        print('N°. INVÁLIDO!', end='')
    else:
        print('+ ' * 20)
        print(f'As notas de {lista[nota][0]} foram {lista[nota][1:]}')
        print('+ ' * 20)
        print()
print('FIM! do programa VOLTE SEMPRE!')
