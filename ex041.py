# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# -  Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

print("\033[36mInscrição para o campeonato de natação!\033[m")
print()
print("-=-"*20)
print()
import datetime
a = str(input("Informe seu nome: "))
b = int(input("Informe seu ano de nascimento: "))
c = datetime.date.today().year
if c - b <= 9:
    print("A sua inscrição foi realizada, {} ! Sua categoria é MIRIM.".format(a.title()))
elif 9 < c - b <= 14:
    print("A sua incrilçao foi realizada, {} ! Sua categoria é INFANTIL".format(a.title()))
elif 14 < c - b <= 19:
    print("A sua inscrição foi realizada, {} ! Sua categoria é JUVENIL".format(a.title()))
elif c - b == 20:
    print("A sua incrição foi realizada, {} ! Sua categoria é SENIOR".format(a.title()))
else:
    print("A sua inscrição foi realizada, {} ! Sua categoria é MASTER".format(a.title()))
print()
print("-=-"*20)
print()
print("\033[34mO processo de inscrição foi realizado com êxito!\033[m")
