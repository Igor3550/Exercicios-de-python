# faça um programa que leia o nome, idade, e sexo de quatro pessoas, no final do programa, mostre:
# a média de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
media = 0
homem = ''
idad = 0
mulheres = 0
medi = 0
for c in range(1, 5):
    print('*' * 30)
    nome = str(input('Digite nome da {}ª pessoa: '.format(c))).title()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa: '.format(c))).strip().upper()
    medi += idade
    if sexo == 'MASCULINO' and idade > idad:
        idad = idade
        homem = nome
    elif sexo == 'FEMININO' and idade <= 20:
        mulheres += 1
    print('')
media = medi/4
print('A média entre todas as idades é de {} anos'.format(int(media)))
print('O homem mais velho é o {}'.format(homem))
print('{} mulheres tem menos de 20 anos'.format(mulheres))
