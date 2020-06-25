#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
print('\n{:*^40}\n'.format(' Desafio013 '))
sal = float(input('Digite seu salario: '))
au = (sal * 15) / 100
salau = sal + au
print('Seu salario é: R$ {:.2f}\nCom 15% de aumento: R$ {:.2f}' .format(sal, salau))
