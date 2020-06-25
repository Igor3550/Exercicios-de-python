#faça um programa que leia a nota de um aluno e calcule sua media mostrando uma mmensagem no finnal de acordo com a media
# abaixo da media 5.0 REPROVADO
# media entre 5.0 e 6.9 RECUPERAÇÃO
# media 7.0 ou superior APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média foi {:.2f} e está REPROVADO!'.format(m))
elif m >= 5 and m < 6.9:
    print('Sua média foi {:.2f} e está de RECUPERAÇÃO!'.format(m))
else:
    print('Sua média foi {:.2f} e está APROVADO!'.format(m))
