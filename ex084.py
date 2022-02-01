# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

import time
print()
print('-=-'*30)
print('Cadastro de pessoas')
print('-=-'*30)
print()
listagem, dados, pesado, leve = [], [], [], []
u = 0
while True:
    a = input(str('Digite seu nome: ')).title()
    b = float(input(f'Informe seu peso, em kg, {a} :'))
    dados.append(a)
    dados.append(b)
    listagem.append(dados[:])
    u = u + 1
    print('Informações cadastradas com sucesso.')
    dados.clear()
    c = input(str('Deseja continuar [S/N]? ')).title().strip()[0]
    if c != 'S' and c != 'N':
        print('Comando inválido. Digite novamente.')
        c = input(str('Deseja continuar [S/N]? ')).title().strip()[0]
    elif c == 'N':
        break
for i in listagem:
    if i[1] > 80:
        pesado.append(i[0])
    elif i[1] < 50:
        leve.append(i[0])
print('Cadastros concluídos')
print()
print('-=-'*30)
print()
print('Analisando os dados cadastrados...')
time.sleep(1)
print('Por favor, aguarde.')
time.sleep(2)
if u == 1:
    print('Foi cadastrada {} pessoa.'.format(u))
else:
    print('Foram cadastradas {} pessoas.'.format(u))
if len(pesado) == 0:
    print('Nenhuma pessoa considerada pesada foi cadastrada')
elif len(pesado) == 1:
    print('A única pessoa considerada pesada foi {}'.format(pesado))
elif len(pesado) > 0:
    print(f'A lista com as pessoas consideradas pesadas é a seguinte: {pesado}')
if len(leve) == 0:
    print('Nenhuma pessoa considerada leve foi cadastrada.')
elif len(leve) == 1:
    print('A única pessoa considerada leve foi {}'.format(leve))
elif len(leve) > 0:
    print('A lista com as pessoas consideradas leves é a seguinte: {}'.format(leve))
