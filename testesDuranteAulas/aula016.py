# tuplas são variaveis compostas; tuplas são imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(sorted(lanche))
for c in lanche:
    print(f'Vou comer um {c}')
print('OUTRA MANEIRA:')
for cont in range(0, len(lanche)):
    print(f'Vou comer um {lanche[cont]} no {cont}')
print(f'Comi {len(lanche)} lanches!')
print('OUTRA MANEIRA ENUMERADA!')
for pos, comida in enumerate(lanche):
    print(f'Vou comeer um {comida} no {pos}')
print('- ' * 40)
print('')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))#contar quantos 'n' existem
print(c.index(2, 1))# posição do 'n' , apartir da 1 posição
print(sorted(c))
del(a)#deleta uma tupla
