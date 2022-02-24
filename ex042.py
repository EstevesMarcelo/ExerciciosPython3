# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

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
    if c1 != c2 != c3 != c1:
        print("É possível formar um triângulo com os 3 segmentos de reta apresentados, onde o mesmo será escaleno.")
    elif c1 == c2 != c3 or c1 == c3 != c2 or c2 == c3 != c1:
        print("É possível formar um triângulo com os 3 segmentos de reta apresentados, onde o mesmo será isósceles. ")
    elif c1 == c2 == c3:
        print("É possível formar um triângulo com os 3 segmentos de reta apresentados, onde o mesmo será equilátero.")
else:
    print("Não é possível formar um triângulo com 3 segmentos de reta apresentados")
print("-=-"*20)
print("Seu analisador foi encerrado")
