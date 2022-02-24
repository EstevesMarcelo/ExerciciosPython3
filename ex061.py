# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a0 = float(input('Informe o primeiro termo da progressão aritmética: '))
r = float(input('Informe a razão da progressão aritmética: '))
i = 0
s = []
while i < 10:
    b = a0 + r*i
    s = s + [b]
    i += 1
print("Os 10 primeiros termos da progressão aritmética cuja razão é {} e primeiro termo {} são:\n{}".format(r, a0, s))
