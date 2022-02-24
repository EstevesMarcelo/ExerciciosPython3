# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print("\033[32mPrograma de alistamento militar!\033[m")
print()
print("-=-"*20)
print()
import datetime
a = str(input("Qual o seu nome completo? "))
b = int(input("Em que ano você nasceu, {}? ".format(a.title())))
c = datetime.date.today().year
if c - b == 18:
    print("Você deve se alistar esse ano, {}".format(a.title()))
elif c - b < 18:
    d = c - b
    e = 18 - d
    if d == 17:
        print("Ainda resta {} ano para seu alistamento, {}.".format(e, a.title()))
    else:
        print("Ainda restam {} anos para seu alistamento, {}.".format(e, a.title()))
else:
    f = c - b
    g = f - 18
    if f == 19:
        print("Seu prazo de alistamento já excedeu há 1 ano, {}.".format(a.title()))
    else:
        print("Seu prazo de alistamento excedeu há {} anos, {}.".format(g, a.title()))
print()
print("-=-"*20)
print()
print("\033[32mNosso analisador foi concluído com êxito\033[32m")
