# Crie um programa que gerencie o aproveitamento de um jogador de futebol.O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print('-=-'*30)
print(f'\033[36m{"Geranciador de aproveitamento":^80}\033[m')
print('-=-'*30)
print()
gen = dict()
gols = []
u = 0
gen['Nome'] = str(input('Nome do jogador: '))
b = int(input('Quantos jogos foram disputados pelo jogador? '))
for i in range(1, b+1):
    c = int(input(f'Quantos gols o jogador fez na partida {i}? '))
    gols.append(c)
    u = u + c
gen['Gols'] = gols[:]
gen['Total'] = u
print()
print('-=-'*30)
print(f'\033[36m{"Resultado":^80}\033[m')
print('-=-'*30)
print(f'O jogador analisado é {gen["Nome"]}')
for v, t in enumerate(gen['Gols']):
    print(f'Na partida {v + 1} ele fez {t} gols')
