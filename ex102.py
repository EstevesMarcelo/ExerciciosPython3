# Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outros chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
# tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    -> Função para o cálculo do fatorial de um número
    :param num: indica o valor numérico para o cálculo do fatorial
    :param show: indica se o usuário deseja visualizar o processo de cálculo do fatorial
    :return: retorna o resultado da operação
    """
    u = 1
    if show is False:
        for i in range(num, 0, -1):
            u = u * i
        return u
    elif show is True:
        print(f'{num}! =', end=' ')
        for i in range(num, 0, -1):
            u = u * i
            if i != 1:
                print(f'{i} X', end=' ')
            elif i == 1:
                print(f'{i} =', end=' ')
        print(f'{u}')


# programa principal
print(fatorial(6, True))
