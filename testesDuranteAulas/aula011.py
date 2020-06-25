# cores
# style 0,1,4,7
# text 30,31,32,33,34,35,36,37
# back 40,41,42,43,44,45,46,47
# \033[0;33;44m
print('\033[4;30;45mTeste\033[m')
print('\033[1;37;44mTeste\033[m')
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'pretobranco': '\033[7;30m'}
print('cores em {}azul{}'.format(cores['azul'], cores['limpa']))
n1 = '7'
res = int(n1) /2
print(type(res))
