from ex107 import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10)}')
