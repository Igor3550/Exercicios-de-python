# listas compostas
test = []
test.append('Igor')
test.append(20)
galera = []
galera.append(test[:])
test[0] = 'maria'
test[1] = 25
galera.append(test)
totmai = totmen = 0
print(galera)
print('-' * 30)
galera = [['joão', 19], ['Ana', 33], ['Joaquim', 15], ['Maria', 45]]
print(galera[3][0][0])
for p in galera:
    print(f'{p[0]} > {p[1]}')
print('-' * 30)
galera = []
dado = list()
for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for pe in galera:
    if pe[1] >= 21:
        print(f'{pe[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{pe[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
