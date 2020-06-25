# Dicionarios
pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade': 20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) #chaves do dicionario
print(pessoas.values())#valores das chaves
print(pessoas.items())#mostra os itens do dicionario
print()
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(k, v)
print()

for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

del pessoas['sexo']# deleta uma chave
pessoas['peso'] = 72# adiciona uma nova chave
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
# Dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print()
brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())# cópia de um dicionario
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
