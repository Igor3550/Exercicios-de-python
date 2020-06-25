# Faça um programa que mostre a tabuada de varios números, um de cada vez
# para cada valor digitado pelo usuário. O programa será interrompido quando o usuário digitar um valor negativo
while True:
    num = int(input('Digite um valor para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
print('FIM!!!')
