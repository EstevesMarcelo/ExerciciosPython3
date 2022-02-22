# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.

from time import sleep
print("Vamos analisar segmentos de reta")
print("-=-"*20)
c1 = float(input("Digite o comprimento do primeiro segmento de reta: "))
c2 = float(input("Digite o comprimento do segundo segmento de reta: "))
c3 = float(input("Digite o comprimento do terceiro segmento de reta: "))
print()
print("Analisando...")
print()
sleep(1)
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    print("É possível formar um triângulo com os 3 sgmentos de retas apresentados")
else:
    print("Não é possível formar um triângulo com 3 segmentos de retas apresentados")
print("-=-"*20)
print("Seu analisador foi encerrado")
