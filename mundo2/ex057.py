# faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'
# Caso esteja errado peça a digitação novamente até ter um valor correto
resp = str(input('Digite o sexo: [M/F] ')).upper()
while resp not in 'MF':
    resp = str(input('Desculpe dados inválidos, tente novamente: ')).upper()
print('Dados aceitos!!')
print('Obrigado!')
