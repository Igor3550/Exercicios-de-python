# faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador,
# e quantos gols ele marcou
# o programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente


def ficha():
    nome = str(input('Nome do jogador: '))
    if nome.strip() == '':
        nome = '<desconhecido>'
    gols = str(input('Numero de gols: '))
    if gols == '' or not gols.isnumeric():
        gols = 0
    return nome, gols


# programa principal
result = ficha()
print(f'O jogador {result[0]} fez {result[1]} gol(s) no campeonato')
