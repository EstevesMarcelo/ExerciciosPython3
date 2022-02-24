# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# a) Média abaixo de 5.0: REPROVADO
# b) Média entre 5.0 e 6.9: RECUPERAÇÃO
# c) Média 7.0 ou superior: APROVADO

print("\033[36mAnalisador de médias!\033[m")
print()
print("-=-"*20)
print()
a = float(input("Informe a primeira média do aluno: "))
b = float(input("Informe a segunda média do aluno: "))
c = (a+b)/2
if c >= 7.0:
    print("Você foi aprovado direto. Parabéns!")
elif c <= 3.0:
    print("Você foi reprovado por média.")
else:
    print("Você precisará fazer uma prova final.")
print()
print("-=-"*20)
print()
print("\033[36mA situação escolar do aluno foi analisada e concluída!\033[m")
