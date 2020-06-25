# faça um programa que leia vários números inteiros pelo teclado
# no final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# o programa deve perguntar ao  usuário se ele quer ou não continuar a digitar os valores
n = soma = maior = menor = media = cont = 0
continuar = 'S'
while continuar != 'N':
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / cont
print('A média entre todos os {} valores foi {:.2f}, o maior valor foi {} e o menor foi {}'.format(cont, media, maior, menor))
