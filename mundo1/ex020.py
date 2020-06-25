# faça um programa que leia os quatro nomes dos alunos e sorteie a ordem de apresentação do trabalho
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
x = [a1, a2, a3, a4]
random.shuffle(x)
print('A ordem de apresentação é {}'.format(x))
