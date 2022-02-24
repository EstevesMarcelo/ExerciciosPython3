# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from time import sleep
print("\033[36mCalculadora de IMC. Iniciando...\033[m")
print()
print("-=-"*20)
print()
a = float(input("Informe o seu peso, em quilogramas: "))
b = float(input("Informe sua altura, em metros:"))
c = a/b**2
print()
print("Estamos aferindo seus dados. Aguarde um momento...")
sleep(2)
print()
if c < 18.5:
    print("Seu índice de massa corporral atual é {:.2f} e você se encontra abaixo do peso ideal.".format(c))
elif 18.5 <= c <= 25:
    print("Seu índice de massa corporal atual é {:.2f} e você se encontra dentro da faixa de peso ideal.".format(c))
elif 25 < c <= 30:
    print("Seu índice de massa corporal atual é {:.2f} e você se encotra acima do peso ideial.".format(c))
elif 30 < c <= 40:
    print("Seu índice de massa corporal atual é {:.2f} e você se encontra em obesidade.".format(c))
else:
    print("Seu índice de massa corpotal atual é {:.2f} e você se encotnra em obesidade mórbida.".format(c))
print()
print("-=-"*20)
print()
print("\033[36mSeu IMC foi calculado. Encerrando calculadora...\033[m")
