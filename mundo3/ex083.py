# faça um programa que o usuario digite uma expressão qualquer que use parenteses.
# seu aplicativo devera analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta
abre = fecha = 0
exp = input('Digite uma expressão: ').strip().replace(' ', '')
print(exp)
for c, v in enumerate(exp):
    if v == '(':
        abre += 1
    elif v == ')':
        fecha += 1
if abre == fecha:
    print('A expressão esta correta!')
else:
    print('A expressão digitada não é válida!')
