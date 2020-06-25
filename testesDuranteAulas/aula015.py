#interromper um laço while
soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
print(f'A soma foi: {soma}')
