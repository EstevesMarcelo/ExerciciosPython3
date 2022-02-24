# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# a) O primeiro valor é maior
# b) O segundo valor é maior
# c) Não existe valor maior, os dois são iguais

print("\033[36mIniciando o comparador de números...\033[m")
print()
print("-=-"*20)
print()
a = int(input("Digite o primeiro número que deseja usar na análise: "))
b = int(input("Digite o segundo número que deseja usar na análise: "))
if a > b:
    print("O primeiro valor é o maior. ")
elif b > a:
    print("o segundo valor é o maior. ")
else:
    print("Os números indicados são iguais. ")
print()
print("-=-"*20)
print()
print("O comparador numérico foi concluído!")
