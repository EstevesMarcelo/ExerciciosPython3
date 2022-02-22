# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("Qual a distância será percorrida na sua viagem, em km/h?"))
if dist <= 200:
    print("Você pagará por essa viagem R$ {}".format(dist*0.50))
else:
    print("Você pagará por essa viagem R$ {}".format(dist*0.45))
