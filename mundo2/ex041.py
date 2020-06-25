# A confederação nacional de natação precisda de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# Até 9 anos MIRIM
# Até 14 anos INFANTIL
# Até 19 anos JUNIOR
# Até 20 anos SêNIOR
# Acima MASTER
from datetime import datetime
ano = int(input('Em que ano você nasceu? '))
idade = datetime.today().year - ano
if idade <= 9:
    print('Você tem {} anos e é classificado como MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e é classificado como INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e é classificado como JUNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e é classificado como SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos e é classificado como MASTER!'.format(idade))
