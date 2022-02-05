# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela.

a = str(input('Digite o nome do aluno: ')).title().strip()
b = float(input('Qual a média do aluno: '))
boletim = {'Nome do aluno': a, 'Média': b}
if b >= 7:
    c = 'Aprovado'
    boletim['Situação'] = c
elif b < 7:
    c = 'Reprovado'
    boletim['Situação'] = c
print(boletim)
