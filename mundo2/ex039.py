# faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se ja passou do tempo se alistamento
# Seu programa tambem deve mostrar o tempo que falta ou que passou do prazo
from datetime import datetime
nome = str(input('Digite seu nome: '))
ano = int(input('Em que ano você nasceu? '))
idade = datetime.today().year - ano
if idade < 18:
    print('{} você é homem e ainda vai se alistar no serviço militar, ainda faltam {} anos'.format(nome, 18 - idade))
elif idade == 18:
    print('Você ja precisa se alistar no serviço militar!')
else:
    print('Já passou {} anos do prazo para seu alistamento!'.format(idade - 18))
