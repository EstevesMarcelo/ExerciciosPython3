# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
# graus Fahrenheit.

temperatura = float(input("Digite a tempueratura para conversão em graus celsius"))
newtemp = (1.8*temperatura)+32
print("A temperatura convertida para graus fahrenheit é de {: .2f} F°".format(newtemp))
