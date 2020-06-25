# fatiamento
frase = 'Curso em Video Python'
print(frase)
print(frase[2:20:2])
print(frase.upper().count('O'))
# analise
print(frase.count('a'))
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('em'))
print('em' in frase)
# transformação
print(len(frase.strip())) #exclui os espaços vazios
print(frase.replace('Python', 'android'))# troca palavras
print(frase)
print(len(frase.split()))#separa cada palavra
divi = frase.split()
print(divi[0][1])#separar letras por coordenadas
print(divi[0].find('u'))#encontrar as coordenadas de letras
print('*'.join(divi))# Coloca algo entre palavras
