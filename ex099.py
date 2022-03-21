# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    cont = Maior = 0
    for i in num:
        cont = cont + 1
        if i > Maior:
            Maior = i
    if cont == 0:
        print('Nenhum valor foi passado ao programa.')
    elif cont == 1:
        print(f'O único número passado foi {i} e, portanto, é o maior valor.')
    elif cont > 1:
        print(f'Os números passados foram {num}.\nForam passados ao todo {len(num)} números.\nO maior número foi'
              f' {Maior}.')
    print('-=-'*30)

maior(2, 3, 4)
maior()
maior(2)
