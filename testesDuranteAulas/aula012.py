# condição aninhada
nome = str(input('Qual seu nome?'))
if nome == 'igor':
    print('Que nome lindo!')
elif nome == 'pedro' or nome == 'maria' or nome == 'matheus':
    print('Seu nome é bem comum no Brasil!')
elif nome in 'ana caludia jessica juliana':
    print('Lindo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('tenha um bom dia, {}!'.format(nome))
