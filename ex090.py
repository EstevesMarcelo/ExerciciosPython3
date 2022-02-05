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
print('-=-'*30)
print(f'O nome do aluno é {boletim["Nome do aluno"]}')
print(f'A média do aluno foi {boletim["Média"]}')
print(f'O aluno está {boletim["Situação"]}')
