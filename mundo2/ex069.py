# faça um programa que leia a idade e o sexo de várias pessoas
# a cada pessa cadastrada o programa deverá perguntar ao usuario se ele quer ou não continuar no final mostre
# quantas pessoas tem mais de 18 anos
# quantos homens
# quantas mulheres tem menos de 20 anos

homens = mulheres = pessoas = cont = 0
print('')
while True:
    print('+ ' * 20)
    idade = (input('Qual a idade: '))
    while not idade.isnumeric():
        idade = (input('Qual a idade: '))
    idade = int(idade)
    sexo = str(input('Qual o sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo: [M/F] ')).strip().upper()
    cont += 1
    if idade >= 18:
        pessoas += 1
    if sexo in 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    print('')
print('')
print('+ ' * 20)
print(f'Foram cadastradas {cont} pessoas!')
print(f'{pessoas} pessoas tem mais de 18 anos')
print(f'Total de {homens} homens')
print(f'E {mulheres} mulheres tem menos de 20 anos')
print('+ ' * 20)
