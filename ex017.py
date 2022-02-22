# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.

#Solução 1
'''import math
a = float(input("Informe o cateto oposto do triângulo retângulo"))
b = float(input("Informe o cateto adjacente do triângulo retângulo"))

s = math.sqrt(a**2 + b**2)
print("A hipotenusa desse triângulo retângulo é {: .2f}".format(s))'''

#Solução 2

import math
a = float(input("Informe o cateto oposto do triângulo retângulo"))
b = float(input("Informe o cateto adjacente do triângulo retângulo"))

s = math.hypot(a,b)
print("A hipotenusa desse triângulo retângulo é{: .2f}.".format(s))
