# faça um programa que leia nome, idade e sexo de várias pessoas, guardando os dados de cada pessoa em um dicionario
# e todos os dicionarios em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todos as pessoas com idade acima da média
pessoas = dict()
lista = list()
idades = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    pessoas['idade'] = int(input('Idade: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while pessoas['sexo'] not in 'MmFf':
        print('Erro! Digite apenas M ou F')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    lista.append(pessoas.copy())
    idades += pessoas['idade']
    resp = str(input('Deseja continuar: [S/N]')).upper()[0]
    while resp not in 'NnSs':
        print('Erro! Digite apenas S ou N')
        resp = str(input('Deseja continuar: [S/N]')).upper()[0]
    if resp in 'Nn':
        break
print('+ ' * 25)
print(f'- O grupo tem {len(lista)} pessoas')
media = idades / len(lista)
print(f'- A média de idade é de {media:.2f} anos')
for m in lista:
    if m['sexo'] in 'Ff':
        print(f'- As mulheres cadastradas foram: {m["nome"]}', end=' ')
print()
print('- Lista com as pessoas acima da média:')
for a in lista:
    if a['idade'] > media:
        for k, v in a.items():
            print(f'{k} = {v}', end=' ')
        print()
print('+ ' * 25)
print()
print('<<ENCERRADO>>')
print(lista)
