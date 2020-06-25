nome = input('Qual seu nome ')
# normal
print('Prazer em te conhecer {}!' .format(nome))

# com 20 espaços
print('Prazer em te conhecer {:20}!' .format(nome))

# alinhado a direita
print('Prazer em te conhecer {:>20}!' .format(nome))

# alinhado a esquerda
print('Prazer em te conhecer {:<20}!' .format(nome))

# centralizado
print('Prazer em te conhecer {:^20}!' .format(nome))

# centralizado com algo (=+*#@!)
print('Prazer em te conhecer {:=^20}!' .format(nome))
