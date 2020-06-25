# Crie um codigo que teste se o site pudim esta acessivel pelo computador usado

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')

print('Buscando Código fonte do site:')
htmlDoSite = str(site.read())
print(htmlDoSite)
