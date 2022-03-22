# Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# a) Quantidade de notas
# b) A maior nota
# c) A menor nota
# d) A média da turma
# e) A situação (opcional)
# Adicione também as docstrings da função

def notas(*nota, sit=False):
    """
    -> Função que cria um dicionário com as informações estatísticas das notas
    :param nota: recebe as notas fornecidas pelo usuário
    :param sit: valor opcional indicando se deve ou não indicar a situação
    :return: retorna um dicionário com várias informações da turma
    """
    c = 0
    a = len(nota)
    dados = {}
    dados['Total'] = len(nota)
    dados['Maior'] = max(nota)
    dados['Menor'] = min(nota)
    for i in nota:
        c = c + i
    media = c / a
    dados['Média'] = media
    if sit == True:
        if media < 5:
            dados['Situação'] = 'Ruim'
        elif 5 <= media < 7:
            dados['Situação'] = 'Regular'
        elif media >= 7:
            dados['Situação'] = 'Bom'
    return dados





# programa principal
b = notas(2,3,5.5,4, sit=True)
print(b)
