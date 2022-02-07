# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
print('-=-'*30)
print(f'{"Arremesso de dados":^80}')
print('-=-'*30)
a = str(input('Nome do primeiro jogador: ')).title().strip()
b = str(input('Nome do segundo jogador: ')).title().strip()
c = str(input('Nome do terceiro jogador: ')).title().strip()
d = str(input('Nome do quarto jogador: ')).title().strip()
print()
sleep(2)
print('Certo. Vamos sortear os números do dados. Boa sorte!')
sleep(2)
e, f, g, h = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
resultado = {
    'Jogador 1': {
        'Nome': a,
        'Nº sorteado': e
    },
    'Jogador 2': {
        'Nome': b,
        'Nº sorteado': f
    },
    'Jogador 3': {
        'Nome': c,
        'Nº sorteado': g
    },
    'Jogador 4': {
        'Nome': d,
        'Nº sorteado': h
    }
}
print()
print('-=-'*30)
print(f'{"Resultados":^80}')
print('-=-'*30)
print()
for i in resultado.keys():
    print(f'O jogador {resultado[i]["Nome"]} tirou o número {resultado[i]["Nº sorteado"]} no dado.')
