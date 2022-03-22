# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    """
    -> Função para fichamento de jogador e gols marcados pelo mesmo
    :param nome: informa o nome do jogador
    :param gols: informa a quantidade de gols marcado pelo jogador
    :return: retorna a situação do jogador no campeonato
    """
    print(f'O jogador {nome} fez {gols} gols')


# programa principal
print('----------')
a = str(input('Nome do jogador: '))
b = str(input('Número de gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(gols=b)
else:
    ficha(a, b)
