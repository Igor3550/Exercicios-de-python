# Refaça o exercicio 035 acrescentando o recurso de mostrar que tipo de triangulo sera formado
# Equilatero todos os lados iguais
# Isosceles dois lados iguais
# Escaleno todos os lados diferentes
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r2 + r3) >= r1 and (r1 + r2) >= r3 and (r3 + r1) >= r2:
    print('As tres retas podem formar um triangulo')
    if r1 == r2 == r3:
        print('E forma um triangulo EQUILATERO!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('E forma um triangulo ISOSCELES!')
    else:
        print('E forma um triangulo ESCALENO!')
else:
    print('As tres retas não formam um triangulo')
