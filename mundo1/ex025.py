#crie um programa que leia e diga se o nome de umaa pessoa te 'SILVA' no nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Você tem "SILVA" no nome: {}'.format('SILVA' in nome.upper()))
