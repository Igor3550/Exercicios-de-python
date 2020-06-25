# funções
def l():
    print('+ ' * 20)


def soma(a, b):
    print('+ ' * 15)
    print(f'A vale {a} e B vale {b}')
    s = a + b
    print(f'A soma de A e B vale {s}')


# programa principal
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)


# empacotar parametros


def contador(*num):
    tam = len(num)
    s = 0
    for n in num:
        s += n
    print(f'Recebi os valores {num} ao todo são {tam} numeros e a soma foi: {s}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# programa principal
l()
contador(1, 4, 3)
contador(5, 8, 3, 9, 5)
contador(12, 3)
l()

print()
l()
print('Drobrar valores')
lista = [1, 5, 3, 9, 6, 2]
print(f'Lista normal {lista}')
dobra(lista)
print(f'Lista Dobrada {lista}')
l()
