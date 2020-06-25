# faça um programa que leia nome e media de um aluno guardando também a situação em um dicionario.
# No final mostre o conteúdo da estrutura na tela.
resul = dict()
resul['Nome'] = str(input('Nome: '))
resul['Media'] = float(input(f'Media de {resul["Nome"]}: '))
if resul['Media'] >= 6:
    resul['Situação'] = 'Aprovado'
elif 6 > resul['Media'] >= 5:
    resul['Situação'] = 'Recuperação'
else:
    resul['Situação'] = 'Reprovado'
for k, v in resul.items():
    print(f'{k}: {v}')
