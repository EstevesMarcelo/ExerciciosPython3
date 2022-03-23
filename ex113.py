# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(numero):
    """
    -> Função para reconhecimento de valores numéricos inteiros
    :param numero: recebe o valor para ser reconhecido pelo programa
    :return: retorna o valor numérico digitado
    """
    ok = False
    valor = 0
    while True:
        try:
            d = str(input(numero))
            valor = int(d)
            ok = True
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuário\033[m')
        if ok:
            break
    return valor


def leiafloat(numero):
    """
    > Função para reconhecimento de valores numéricos reais
    :param numero: recebe o valor para ser reconhecido pelo programa
    :return: retorna o valor numérico digitado
    """
    ok = False
    valor = 0
    while True:
        try:
            d = str(input(numero))
            valor = float(d)
            ok = True
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número real.\033[m')
        if ok:
            break
    return valor


# programa principal
b = leiaint('Digite um número inteiro: ')
c = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {b} e o número real {c}.')
