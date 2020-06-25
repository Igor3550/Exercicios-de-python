# crie um programa que tenha uma função chamada voto() que vai receber como parametros a data de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições


def voto(ano):
    from datetime import datetime  # escopo de importação, a impoportação só funciona dentro da função
    idade = datetime.today().year - ano
    if idade < 16:
        v = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade < 65:
        v = 'VOTO OPCIONAL'
    else:
        v = 'VOTO OBRIGATÓRIO'
    return idade, v


# programa principal
nasc = int(input('Em que ano voce nasceu? '))
result = voto(nasc)
print(f'Com {result[0]} anos: {result[1]}')
