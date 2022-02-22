# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

import math
a = float(input("Informe o valor do ângulo"))
b = math.radians(a)
print("O seno de {: .2f} é {: .2f}, seu cosseno é {: .2f} e sua tangente é {: .2f}".format(a, math.sin(b), math.cos(b), math.tan(b)))