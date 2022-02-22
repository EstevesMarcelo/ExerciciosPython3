# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Quantos metros possui sua peça?"))
print("Convertendo as unidades, sua peça possui {} centímetros ou {} milímetros".format(medida*100, medida*1000))
