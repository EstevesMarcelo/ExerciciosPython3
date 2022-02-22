# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carrocusta R$60 por dia
# e R$0,15 por Km rodado.

quilometro = float(input("Qual a distância percorrida, em quilômetros, pelo carro?"))
dias = int(input("Quantos dias você utilizou o carro?"))

a1 = quilometro*0.15
a2 = dias*60
s = a1 + a2

print("O total a pagar pela utilização do veículo é de R${}".format(s))
