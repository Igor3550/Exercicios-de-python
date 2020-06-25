def leiaDinheiro(val):
    while True:
        resul = str(input(val)).strip()
        teste = resul
        if ',' in teste:
            teste = teste.replace(',', '')
            if teste.isnumeric():
                resul = resul.replace(',', '.')
                r = float(resul)
                break
        elif '.' in teste:
            teste = teste.replace('.', '')
            if teste.isnumeric():
                r = float(resul)
                break
        elif resul.isnumeric():
            r = float(resul)
            break
        else:
            print(f'\033[1:31mErro! O valor "{resul}" não é um preço válido!\033[m')
    return r
