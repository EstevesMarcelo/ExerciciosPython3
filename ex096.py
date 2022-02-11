# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(compr, larg):
    s = compr * larg
    m = round(s, 2)
    print(f'A área do terreno retangular é {m} m².')


compr = float(input('Qual o comprimento do terreno, em metros? '))
larg = float(input('Qual a largura do terreno, em metros? '))
area(compr, larg)
