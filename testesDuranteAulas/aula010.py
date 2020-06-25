# condição simples
print('{:*^40}'.format('condição simples'))
print('Escolha um menu: \n1. Nomes\n2. Calcular media')
esc = int(input('Menu: '))
if esc == 1:
    print('{:*^40}'.format('Condiçoes com nomes'))
    nome = str(input('Digite seu nome: '))
    if nome == 'Igor':
        print('Que nome lindo voce tem!')
    print('Bom dia {}!'.format(nome))
    # condição composta
    print('{:*^40}'.format('condição composta'))
    nome = str(input('Digite seu nome: '))
    if nome == 'Igor':
        print('seu nome é massa {}'.format(nome))
    else:
        print('seu é considerado comum')
    print('Bom dia, {}'.format(nome))
else:
    # condiçao
    print('{:*^40}'.format('calcular media'))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = (n1 + n2) / 2
    print('Sua média foi {:.1f}'.format(m))
    if m >= 6.0:
        print('sua média foi boa!')
    else:
        print('sua média não foi tão boa')
