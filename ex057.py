# Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

from time import sleep
n = ""
while n != "M" and n != 'F':
    n = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
    if n != 'M' and n != 'F':
        print("Você informou uma informação de sexo inválida. Por favor, indique novamente seu sexo.")
    else:
        print('Coletando dados')
print()
sleep(1)
print('A informação foi coletada com êxito.')
