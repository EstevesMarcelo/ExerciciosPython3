#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
#de futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o time da Chapecoense.

print('-'*30)
print('\033[36mInformações do brasileirão\033[m')
print('-'*30)
times= ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense','América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional','São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport','Chapecoense')
print(f'Os 5 primeiro colocados do campeonato foram: {times[0:5]}')
print('-'*30)
print(f'Os 4 últimos colocados da tabela foram: {times[16:20]}')
print('-'*30)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-'*30)
for pos,i in enumerate(times):
    if i == 'Chapecoense':
        print(f'O time da {i} está na {pos + 1}ª posição na tabela do campeonato.')
print('-'*30)
