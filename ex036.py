# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.

print("\033[31m Vamos iniciar nossa análise bancária!\033[m")
print()
print("-=-"*20)
print()
valor = float(input("Qual o valor, em reais, da casa que você deseja financiar?"))
salario = float(input("Qual é o seu salário atual, em reais?"))
tempo = int(input("Em quantos anos você pretende quitar seu imóvel?"))
tempo1 = tempo*12
prestacao = valor/tempo1
if salario*0.30 >= prestacao:
    print("Seu financeiamento será aprovado com prestação mensal de R$ {: .2f}".format(prestacao))
else:
    print("Nós precisamos revisar sua proposta, pois as prestações excedem 30% do seu salário e, dessa forma, seu "
          "financeiamento pode ser negado")
print()
print("A análise foi encerrada.")
