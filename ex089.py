# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

print('-=-'*30)
print('Cadastro de alunos')
print('-=-'*30)

boletim, registro, notas, aux = [], [], [], []
while True:
    a = input(str('Digite o nome do aluno: ')).title()
    registro.append(a)
    aux.append(a)
    b = float(input('Qual a primeira nota do aluno? '))
    registro.append((b))
    c = float(input('Qual a segunda nota do aluno? '))
    registro.append(c)
    e = (b + c)/2
    aux.append(e)
    boletim.append(aux[:])
    notas.append(registro[:])
    registro.clear()
    aux.clear()
    print('Aluno e notas cadastrados com sucesso!')
    d = input(str('Deseja cadastrar outro aluno?[S/N] ')).title().strip()[0]
    if d != 'S' and d != 'N':
        print('Comando inválido. Tente novamente.')
        d = input(str('Deseja cadastrar outro aluno?[S/N] ')).title().strip()[0]
    elif d == 'N':
        print('Cadastros de alunos concluídos.')
        break
print()
print('-=-'*30)
print(f'{"Boletim":^90}')
print('-=-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print()
for i, s in enumerate(boletim):
    print(f'{i:<4}{s[0]:<10}{s[1]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qua aluno? (Digite 999 para interromper): '))
    if opc == 999:
        print ('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {notas[opc][1]} e {notas[opc][2]}')
print('<<<VOLTE SEMPRE>>>')
