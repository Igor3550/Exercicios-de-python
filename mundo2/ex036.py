# faça um programa para aprovar o emprestimo bancario para a compra de uma casa .
# o programa vai perguntar o valor da casa o salario do comprador e em quantos anos ele vai pagar
# calcule o valor da prestaçao mensal sabendo que ela nao pode exceder 30% do salario ou então o emprestimo será negado

valorCasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Quanto você ganha? R$'))
tempo = int(input('Em quantos anos você deseja financiar? '))

tempo = tempo * 12
prestacao = valorCasa / tempo
limite = (sal * 30 / 100)

if prestacao > limite:
    print('Desculpe, seu empréstimo NÃO foi aprovado!')
else:
    print('Parabéns, seu empréstimo foi aprovado com sucesso!')
    print('Valor da mensalidade em {}x de R${:.2f}'.format(int(tempo), prestacao))
