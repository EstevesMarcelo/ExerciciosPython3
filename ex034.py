# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salário: "))
if salario > 1250:
    print("O seu novo salário após o aumento de 10% é R$ {: .2f}.".format(salario*1.1))
if salario <= 1250:
    print("O seu novo salário após o aumento de 15% é R$ {: .2f}".format(salario*1.15))
