def aumentar(n, p1=10, p=False):
    """

    :param n: número de análise
    :param p1: taxa de aumento aplicada
    :param p: conversão opcional para unidade monetária
    :return: retorna o resultado da operação
    """
    w = p1 / 100
    if p is True:
        z = n * w
        return moeda(z)
    else:
        return n * w


def diminuir(n, p2=5, p=False):
    """

    :param n: número de análise
    :param p2: taxa de redução aplicada
    :param p: conversão opcional para unidade monetária
    :return: retorna o resultado da operação
    """
    w = p2/100
    if p is True:
        z = n * w
        return moeda(z)
    else:
        return n * w


def dobro(n, p=False):
    """

    :param n: número de análise
    :param p: conversão opcional para unidade monetária
    :return: retorna o resultado da operação
    """
    if p is True:
        z = n * 2
        return moeda(z)
    else:
        return n * 2


def metade(n, p=False):
    """

    :param n: número de análise
    :param p: conversão opcional para unidade monetária
    :return: retorna o resultado da operação
    """
    if p is True:
        z = n / 2
        return moeda(z)
    else:
        return n/2


def moeda(n):
    """
    -> Função para conversão de unidades
    :param n: número de análise
    :return: retorna o valor convertido para forma monetária
    """
    return f'R${n}'


def resumo(n=0, p1=10, p2=5):
    """
    -> Função para exibição de um resumo de análise
    :param n: valor para análise
    :param p1: taxa de aumento
    :param p2: taxa de redução
    :return: retorna o resumo operacional
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{p1}% de aumento: \t{aumentar(n,p1,True)}')
    print(f'{p2}% de redução: \t{diminuir(n,p2,True)}')
    print('-'*30)

