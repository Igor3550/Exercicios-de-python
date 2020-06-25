# Funções avançadas


def teste():
    d = 9
    f = 8  # cria uma nova variavel (local)
    global a1  # evita criar uma variavel local
    print(f'D: A variavel global a1 : {a1}')  # variavel global pode ser usada por "qualque um"
    a1 += 3  # Altera o valor da variavel global
    print(f'D: A variavel global a1 + 3: {a1}')
    print(f'D: A variavel local d: {d}')  # variavel local não pode """
    print(f'D: A variavel local f: {f}')


def soma(a=0, b=0, c=0):  # variaveis opcionais
    s = a + b + c
    return s


def fatorial(num=1):
    # help para a função (DOCSTRING)
    """
    => fatora valores
    :param num: variavel a ser fatorada
    :return f: resultado do fatoramento
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# programa principal
f = 7
a1 = 2
print(f'Fora: A variavel global f: {f}')
print(f'Fora: A variavel global a1: {a1}')
teste()
print(f'Fora: A variavel a1 dps da função: {a1}')

print()

s1 = soma(1, 2, 3)
s2 = soma(1, 2)
s3 = soma()
print(f'As somas foram: {s1}, {s2} e {s3}')

print()

help(fatorial)  # chama o help para a função

r1 = fatorial(8)
r2 = fatorial(6)
r3 = fatorial()
print(f'Os resultados foram {r1}, {r2} e {r3}')
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é {fatorial(n)}')
