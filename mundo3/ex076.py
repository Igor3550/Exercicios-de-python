# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia
# no final mostre uma listagem de preços organizando os dados em forma tabular
produtos = ('Teclado', '85.00', 'Mouse', '55.00', 'Notebook SamSom', '2550.00',
            'Arroz', '12.00', 'Feijão', '8.50', 'Fone', '35.00', 'Açucar', '9.50',
            'Café', '5.50', 'Mesa', '800.00')
c = 0
esp = 0
pontos = 0
print('+ '*28)
while c != len(produtos):
    pontos = len(produtos[c])
    esp = len(produtos[c+1])
    print(f'+ {produtos[c]}{"."*(40-pontos)} R${produtos[c+1]}{" "*(9 - esp)}+')
    c += 2
print('+ '*28)
print('Volte Sempre!')
