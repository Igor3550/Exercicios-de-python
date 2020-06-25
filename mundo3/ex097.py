# faça um programa que tenha uma funpção chamada escreva que receba um texto qualquer e mostre uma mensagem adaptavel
def escreva(txt):
    p = len(txt) + 4
    print('~' * p)
    print(f'  {txt}')
    print('~' * p)


# programa principal
escreva('A cor de ceu é azul!')
escreva('Curso em Video')
escreva('Python')
