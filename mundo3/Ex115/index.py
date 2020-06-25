from time import sleep
from Ex115.uteis.interface import *
from Ex115.uteis.arquivo import *

# programa principal

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criar(arq)

while True:
    esc = menu(['Cadastrar Pessoa', 'Listar Pessoas Cadastradas', 'Sair do Sistema'])
    if esc == 1:
        # Casdastrar novo usuario
        cabecalho('Cadastrar Pessoa')
        nome = str(input('Nome: '))
        idade = valida('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif esc == 2:
        # Ler um arquivo de texto
        lerArquivo(arq)
        sleep(1)
    elif esc == 3:
        break
    else:
        print('\033[31mERRO! digite uma opção válida!\033[m')
        sleep(2)
cabecalho('Saindo do Sistema... Até logo!')
sleep(1)
