# Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
# de 2 metros quadrados.

largura = float(input("Qual é a largura da parede em metros?"))
altura = float(input("Qual é a altura da parade em metros?"))
print("A área da parede, em metros quadrados, é de {}. Para pintar essa parede, serão necessários {} litros de tinta.".format(altura*largura,(altura*largura)/2))
