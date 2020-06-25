# um professor quer sortear um de seus quatro alunos para apagar o quadro faça um programa que ajude ele, lendo o nome deles e escrevendo o noome do escolhido
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome de segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
x = [a1, a2, a3, a4]
sort = random.choice(x)
print('O aluno escolhido foi {}'.format(sort))
