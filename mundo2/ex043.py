# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mopstre seu status, de acordo com a tabela abaixo
# Abaixo de 18.5 Abaixo do peso
# Entre 18.5 e 25 Peso ideal
# 25 até 30 Sobrepeso
# 30 até 40 Obesidade
# acima de 40 Obesidade mórbida
peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você esta abaixo do peso!'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.2f} e você esta no peso ideal!'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f} e você esta em sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f} e você esta em obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e vecê esta em Obesidade Mórbida!'.format(imc))
