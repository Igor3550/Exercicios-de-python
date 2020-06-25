# faça um  programa que tenha uma tupla com vários palavras
# Depois disso você deve mostrar para cada palavra quais são as suas vogais
palavras = ('amendoin', 'batata', 'mouse', 'teclado', 'curso', 'mesa',
            'cama', 'televisao', 'casa', 'porta', 'sofa', 'tv')
for c in palavras:
    print(f'As vogais de {c} são: ', end='')
    s = 0
    for cont in c:
        if cont in 'aeiou':
            print(f' {cont}', end='')
            s += 1
    if s == 0:
        print('Esta palavra não tem vogais!')
    print('')
print('FIM!!!')
