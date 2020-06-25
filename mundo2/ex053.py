# crie um programa que leia uma frase e diga se ela é um palindromo, desconsidedrando os espaços
frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
comp = len(frase)
inverso = ''
for c in range(comp-1, -1, -1):
    inverso += frase[c]
print('A frase "{}" ao contrário fica "{}"'.format(frase, inverso))
if inverso == frase:
    print('Temos um palíndromo')
else:
    print('A frase não é um palídromo')
