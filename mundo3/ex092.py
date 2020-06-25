# faça um programa que leia nome, ano de nascimento, e carteira de trabalho e cadastre-os (com idade) em um dicionario
# se por acaso o CTPS for diferente de zero o dicionario receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade com quantos anos a pessoa vai se aposentar.
from datetime import datetime
from time import sleep
pessoa = dict()
pessoa['Nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.today().year - ano
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salario: '))
    pessoa['Aposentadoria'] = pessoa['Ano'] + 35
print('+ ' * 20)
print(f'Nome: {pessoa["Nome"]}')
print(f'Idade: {pessoa["Idade"]}')
print(f'CTPS: {pessoa["CTPS"]}')
if pessoa['CTPS'] != 0:
    print(f'Ano de contratação: {pessoa["Ano"]}')
    print(f'Salário: {pessoa["Salario"]:.2f}')
    print(f'Aposentadoria: {pessoa["Aposentadoria"]}')
print('+ ' * 20)
print()
print('Encerrando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
