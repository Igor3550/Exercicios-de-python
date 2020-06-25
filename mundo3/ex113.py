# reescreva a função leiaInt() que fizemos no ex104, incluindo agora a possibilidade de um numero de tipo invalido
# Aproveite e crie tambem a função leiaFloat com a mesma funcionalidade

# definindo algumas cores
vermelho = '\033[31m'
limpa = '\033[m'


# definido as funções
def leiaInt(txt):
    inteiro = str()
    valido = False
    while not valido:
        try:
            inteiro = int(input(txt))
        except ValueError:
            print(f'{vermelho}ERRO: digite um numero inteiro válido!{limpa}')
        else:
            valido = True
    return inteiro


def leiaFloat(txt):
    valido = False
    while not valido:
        try:
            real = float(input(txt))
        except ValueError:
            print(f'{vermelho}ERRO: digite um numero real válido!{limpa}')
        else:
            valido = True
    return real


# programa principal
i = leiaInt('Digite um numero inteiro: ')
r = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
