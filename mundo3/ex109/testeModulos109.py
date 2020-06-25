from ex109 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, f=True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, f=True)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10, f=True)}')
print(f'Diminuindo 15% temos {moeda.diminuir(valor, 15, f=True)}')
