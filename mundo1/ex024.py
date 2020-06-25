#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'SANTO'
cid = str(input('Digite um nome de uma cidade: ')).strip()
veri = cid.upper()#.startswith('SANTO')
# print('Sua cidade começa com "SANTO": {}'.format(veri)) OU
print('Sua cidade começa com "SANTO" : {}'.format(veri[:5] == 'SANTO'))
