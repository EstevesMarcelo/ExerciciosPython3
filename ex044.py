# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print("O preço normal do item é R$150,00.")
print()
a = str(input("De que forma você pretende realizar o pagamento?"))
b = 150.00
print()
if a.title() == "A Vista Dinheiro" or a.title() == "A Vista Cheque":
    print("Você receberá 10% de desconto em sua compra e pagará {:.2f}".format(b*0.9))
elif a.title() == "A Vista No Cartão":
    print("Você receberá 5% de desconto em sua compra  e pagará {:.2f}".format(b*0.95))
elif a.title() == "A Vista No Cartão":
    print("Você pagará o preço normal do produto.")
elif a.title() == "Parcelado No Cartão":
    c = int(input("Em quantas parcelas você pretende dividir a compra? "))
    if c ==2:
        print("Você pagará o preço normal do produto.")
    if c > 2:
        print("Você pagará um juros de 20% sobre o valor de compra, pagando como parcela mensal R$ {} .".format((b*1.2)/c))
