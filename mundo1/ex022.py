# crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas a letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome
print('*' * 40)
nome = str(input('Digite seu nome completo: ')).strip()
print('MAIÚSCULO: {}'.format(nome.upper()))
print('minúsculo: {}'.format(nome.lower()))
s = nome.split()
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome {} tem {} letras'.format(s[0], len(s[0])))
