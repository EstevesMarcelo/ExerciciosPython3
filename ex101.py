# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa,retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.


def voto(ano):
    """
    -> Função verificadora de condição de voto de uma pessoa
    :param ano: ano de nascimento da pessoa analisada
    :return: retorna a condição de voto da pessoa
    """
    from datetime import date
    a = date.today().year
    d = a - ano
    if d < 16:
        return f'O voto é negado para essa pessoa.'
    elif 16 <= d < 18:
        return f'O voto para essa pessoa é opcional.'
    elif 18 <= d <= 65:
        return f'O voto para essa pessoa é obrigatório.'
    elif d > 65:
        return f'O voto para essa pessoa é opcional.'


# programa principal
nasc = int(input("Informe o ano de nascimento da pessoa analisada: "))
print(voto(nasc))
