# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.




#Solução 1
#import math
#a= float(input("Digite um número qualquer"))
#print("A parte inteira de {} é {}. ".format(a, math.floor(a)))

#Solução 2
#from math import trunc
#a= float(input("Digite um número qualquer"))
#print("A parte inteira de {} é {}. ".format(a, trunc(a)))

#Solução 3
a= float(input("Digite um número qualquer"))
print("A parte inteira de {} é {}. ".format(a, int(a)))