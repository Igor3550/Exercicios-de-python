n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# O 'end=' serve para nao haver quebra de linhas
print('A soma é {}\nO produto é {}\nA divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {}\nE potencia {}'.format(di, e))
