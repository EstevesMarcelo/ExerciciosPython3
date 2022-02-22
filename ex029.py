# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Em que velocidade o carro se encontrava, em km/h?"))
a = vel - 80
b = a*7.00
if vel > 80:
    print("Você excedeu o limite de velocidade e será multado em R$ {: .2f}".format(b))
else:
    print("Você se encontrava dentro dos limites de velocidade da via.")
