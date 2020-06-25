# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario
# com as informaçoes: -Quantidade de notas, -A maior nota, -A menor nota, -A média da turma, -A situação (opcional)
# adicione tambem as DOCSTRINGS da função


def notas(*n, sit=False):
    """
    => Função para analisar e situações de varios alunos
    :param n: lista que recebe as notas dos alunos
    :param sit: (opcional) mostra ou não a situação da turma
    :return: retorna um dicionario com as informaçoes
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] < 5:
            r['Situação'] = 'Ruim'
        elif 5 <= r['media'] < 7:
            r['Situação'] = 'Razoavel'
        elif r['media'] >= 7:
            r['Situação'] = 'Boa'
    return r


# programa principal
resp = notas(5, 7, 8, 4, sit=True)
print(resp)
help(notas)
