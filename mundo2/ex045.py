# faça um programa que jogue jokenpô com você
from random import choice
from time import sleep
# Cores
cores = {'limpa': '\033[m', 'laranja': '\033[33m', 'branco': '\033[30m', 'vermelho': '\033[31m', 'amarelo': '\033[32m', 'azul': '\033[34m', 'roxo': '\033[35m', 'ciano': '\033[36m', 'cinza': '\033[37m'}

print('\n{}{:*^40}{} \n'.format(cores['ciano'], ' {}JOKENPÔ{} '.format(cores['azul'], cores['ciano']), cores['limpa']))
print('{}+ '.format(cores['azul']) * 8)
print('{}+ 1- Pedra    +\n{}+ 2- Papel    +\n{}+ 3- Tesoura  +{}'.format(cores['vermelho'], cores['roxo'], cores['laranja'], cores['azul']))
print('+ ' * 8)
esc = int(input('{}\nEscolha sua jogada: '.format(cores['limpa'])))
print('\n{}JO'.format(cores['vermelho']))
sleep(1)
print('{}KEN'.format(cores['roxo']))
sleep(1)
print('{}PÔ!!!\n'.format(cores['laranja']))
escos = [1, 2, 3]
pc = choice(escos)
ganha = 'Pedra'
num = 1
perde = 'Tesoura'
empate = False
op = True
if (esc == 1 and pc == 2) or (pc == 1 and esc == 2):
    ganha = 'Papel'
    perde = 'Pedra'
    num = 2
elif (esc == 1 and pc == 3) or (pc == 1 and esc == 3):
    ganha = 'Pedra'
    perde = 'Tesoura'
    num = 1
elif (esc == 2 and pc == 3) or (pc == 2 and esc == 3):
    ganha = 'Tesoura'
    perde = 'Papel'
    num = 3
elif esc == pc:
    empate = True
    num = esc
    if num == 1:
        ganha = 'Pedra'
    elif num == 2:
        ganha = 'Papel'
    else:
        ganha = 'Tesoura'
else:
    print('Opção de jogada inválida')
    op = False
if op == True:
    if empate:
        print('{}*+'.format(cores['roxo']) * 13)
        print('{}JOGADOR: {}{}'.format(cores['azul'], ganha, cores['limpa']))
        print('{}COMPUTADOR: {}{}'.format(cores['ciano'], ganha, cores['limpa'], ))
        print('{}*+'.format(cores['roxo']) * 13)
        print('\n{}EMPATE!'.format(cores['azul']))
    else:
        if esc == num:
            print('{}*+'.format(cores['roxo']) * 13)
            print('{}JOGADOR: {}{}'.format(cores['ciano'], ganha, cores['limpa']))
            print('{}COMPUTADOR: {}{}'.format(cores['azul'], perde, cores['limpa'],))
            print('{}*+'.format(cores['roxo']) * 13)
            print('\n{}PARABÉNS VOCÊ GANNHOU!'.format(cores['ciano']))
        else:
            print('{}*+'.format(cores['roxo']) * 13)
            print('{}JOGADOR: {}{}'.format(cores['ciano'], perde, cores['limpa']))
            print('{}COMPUTADOR: {}{}'.format(cores['azul'], ganha, cores['limpa'], ))
            print('{}*+'.format(cores['roxo']) * 13)
            print('\n{}VOCÊ PERDEU!'.format(cores['vermelho']))
