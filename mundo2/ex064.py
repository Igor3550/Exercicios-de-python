# faça um programa que leia varios numeros inteiros pelo teeclado,
# o programa só vai parar quando o usuário digitar 999, que é a condição de parada
# no final mostre quantos numeros foram digitados e qual foi a soma entre eles
soma = cont = 0
n = int(input('Digite um valor: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor: '))
print('Você digitou {} numeros e a soma entre foi: {}'.format(cont, soma))
print('FIM!')
