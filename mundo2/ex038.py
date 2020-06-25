# faça um programa que leia dois numeros inteiros  e compare os mostrando na tela uma mensagem
# O primmeiro valor é o maior
# O segundo valor é o mmaior
# Não existe valor maior, os dois são iguais
n = int(input('Digite um numero: '))
n1 = int(input('Digite outro numero: '))
if n > n1:
    print('O primeiro valor é maior!')
elif n1 > n:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
