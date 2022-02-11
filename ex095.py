# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema
# de visualização de detalhes do aproveitamento de cada jogador.

print('-=-'*30)
print(f'\033[36m{"Geranciador de aproveitamento":^80}\033[m')
print('-=-'*30)
print()
gen = dict()
gols, result = [], []
u = 0
while True:
    # aqui serão cadastrados as informações do jogadores
    gen['Nome'] = str(input('Nome do jogador: '))
    b = int(input('Quantos jogos foram disputados pelo jogador? '))
    for i in range(1, b+1):
        c = int(input(f'Quantos gols o jogador fez na partida {i}? '))
        gols.append(c)
        u = u + c
    gen['Gols'] = gols[:]
    gen['Total'] = u
    result.append(gen.copy())
    gen.clear()
    gols.clear()
    u = 0
    a = str(input('Quer continuar?[S/N] ')).title().strip()[0]
    if a != 'S' and a != 'N':
        print('Comando inválido. Tente novamente.')
        a = str(input('Quer continuar?[S/N] ')).title().strip()[0]
    elif a == 'N':
        break
# aqui será formatado a tabela de resultados
print()
print('-=-'*30)
print(f'\033[36m{"Resultado":^80}\033[m')
print('-=-'*30)
print(f'{"COD":<4}{"Jogador":<20}{"Gols":<20}{"Total":<20}')
for v, t in enumerate(result):
    # aqui formataremos as informações dos jogadores obtidas
    print(f'{v:<4}', end='')
    for x in t.values():
        print(f'{str(x):<20}', end='')
    print()
while True:
    # aqui será inicializado o buscador de informações individuais dos jogadores
    busca = int(input('Mostrar dados de qual jogador? (Digite 999 para parar)'))
    if busca == 999:
        break
    elif busca >= len(result):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {result[busca]["Nome"]}')
        for g, h in enumerate(result[busca]["Gols"]):
            print(f'    No jogo {g + 1} faz {h} gols.')
    print('-=-'*30)
print('<<VOLTE SEMPRE>>')
