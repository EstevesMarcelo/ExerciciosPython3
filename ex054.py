# Crie um progrema que leia o ano de nascimento de sete pessoas. No final, mostre
# Quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
a1 = str(input("Digite seu nome: ")).title().strip()
a = int(input("Em que ano você nasceu, {} ?".format(a1)))
b1 = str(input("Digite seu nome: ")).title().strip()
b = int(input("Em que ano você nasceu, {} ?".format(b1)))
c1 = str(input("Digite seu nome: ")).title().strip()
c = int(input("Em que ano você nasceu, {} ?".format(c1)))
d1 = str(input("Digite seu nome: ")).title().strip()
d = int(input("Em que ano você nasceu, {} ?".format(d1)))
e1 = str(input("Digite seu nome: ")).title().strip()
e = int(input("Em que ano você nasceu, {} ?".format(e1)))
f1 = str(input("Digite seu nome: ")).title().strip()
f = int(input("Em que ano você nasceu, {} ?".format(f1)))
g1 = str(input("Digite seu nome: ")).title().strip()
g = int(input("Em que ano você nasceu, {} ?".format(g1)))
m = [a, b, c, d, e, f, g]
n = [a1, b1, c1, d1, e1, f1, g1]

h = datetime.date.today().year
s = []
t = []
w = 0
z = 0
for i in range(0, 7):
    if h - m[i] < 18:
        s += [n[i]]
        w += 1
    else:
        t += [n[i]]
        z += 1
if w == 1:
    print("Apenas uma pessoa é menor de idade, sendo ela {}".format(s[0]))
    print("As 6 pessoas maiores de idade são: {}".format(t))
elif w == 0:
    print("Não há pessoas menores de idade na relação apresentada!")
    print("Todas as pessoas listadas são maiores de idade!")
elif w > 1:
    print('{} pessoas ainda não alcançaram a maioridade, sendo elas: {}.'.format(w, s))
    print('{} pessoas já alcançaram a maioridade, sendo elas: {}.'.format(z, t))
