#faça um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores a 1.200.00 calcule um aumento de 10%
# Para salarios menores ou iguais o aumento é de 15%
sal = float(input('Digite o valor do salario: R$'))
if sal > 1200:
    reaj = sal * 10 / 100
    print('Seu salario era de R${} e com reajuste de 10% passa a ser: R${}'.format(sal, sal + reaj))
else:
    reaj = sal * 15 / 100
    print('Seu salario era de R${} e com reajuste de 15% passa a ser: R${}'.format(sal, sal + reaj))
