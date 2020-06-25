# Listas
num = [2, 5, 9, 1]# cria uma lista
print(num)
num[2] = 3# mostra o elemento da casa 2
print(num)
num.append(7)# adiciona o elemebto 7 a lista
print(num)
num.sort()# ordena a lista
print(num)
num.sort(reverse=True)# ordena a lista de tras para frente
print(num)
num.insert(2, 0)# adiciona 0 na casa 2
print(num)
num.pop(0)# exclui o elemnto da casa 0
print(num)
num.remove(2)# remove o primeiro elemento 2 q aparece
num.insert(2, 2)
print(num)
print('-'*30)
print('')
valores = []
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}')
print('FIM!!!')
print('-'*30)
print('')
a = [2, 5, 6, 4]
b = a# cria uma ligação entre as listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('')
b[2] = 8# altera as duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('')
b = a[:]# cria uma cópia da lista
b[1] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')
