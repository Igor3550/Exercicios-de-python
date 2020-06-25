#faça um programa que leia o nome de uma pessoa mostrando em seguioda o primeiro e o ultimo nome separadamente
#Ex: Ana Maria de Souza
#primeiro nome: Ana
# segundo: Souza
print('{:*^40}'.format(' Desafio 027 '))
nome = input('Digite seu nome completo: ')
nome = nome.title().strip()
print('Nome completo: {}'.format(nome))
nome = nome.split()
sn = len(nome) - 1
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[sn]))
