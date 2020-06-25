# tratamento de erros e exceções
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Ouve um erro com o valor que voce digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except SystemExit:
    print('Usuario pulou fora!')
except KeyboardInterrupt:
    print('Usuario preferio não digitar um valor')
else:
    print(f'O resultado foi: {r}')
finally:
    print('Volte Sempre! muito obrigado!')
