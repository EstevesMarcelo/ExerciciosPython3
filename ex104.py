# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.


def leiaint(numero):
    ok = False
    valor = 0
    while True:
        b = str(input(numero))
        if b.isnumeric():
            valor = int(b)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um número inteiro.\033[m')
        if ok:
            break
    return valor


# programa principal
b = leiaint('Digite um número: ')
print(f'Você digitou o número {b}')
