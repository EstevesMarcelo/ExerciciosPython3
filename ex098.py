# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim
# e passo.Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b)de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print(f'Fazendo a contagem de {ini} a {fim} de {pas} em {pas}. ')
    sleep(2.5)

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += pas
        print('FIM!')

    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= pas
        print('FIM')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=-'*20)
print('Agora é sua vez de personalizar a contagem.')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
