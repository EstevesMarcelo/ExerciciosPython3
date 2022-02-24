# Crie um programa que faça o computador jogar Jokenpô com você.

print("\033[36mVamos jogar jokenpô!\033[m")
print()
print("-=-"*20)
print()
a = ["Pedra", "Papel", "Tesoura"]
import random
from time import sleep
b = random.choice(a)
print("Vamos começar?")
print()
c = str(input('Escolha:Pedra, Papel ou Tesoura?'))
d = c.title()
print()
print("Jo")
sleep(0.5)
print("ken")
sleep(0.5)
print("pô!")
print()
if d == "Pedra" and b == "Pedra":
    print("Eu havia escolhido pedra. Nós empatamos dessa vez xD")
elif d == "Pedra" and b == "Tesoura":
    print("Eu havia escolhido tesoura. Você me venceu :/")
elif d == "Pedra" and b == "Papel":
    print("Eu havia escolhido papel. Eu venci dessa vez \o/")
elif d == "Tesoura" and b == "Pedra":
    print('Eu havia escolhido pedra. Eu venci dessa vez \o/')
elif d == "Tesoura" and b == "Tesoura":
    print("Eu havia escolhido Tesoura. Nós empatamos dessa vez xD")
elif d == "Tesoura" and b == "Papel":
    print("Eu havia escolhido Papel. Você me venceu :/")
elif d == "Papel" and b == "Pedra":
    print("Eu havia escolhido Pedra. Você me vencer :/")
elif d == "Papel" and b == "Tesoura":
    print("Eu havia escolhido Tesoura. Eu venci dessa vez \o/")
elif d == "Papel" and b == "Papel":
    print("Eu havia escolhido Papel. Nós empatamos dessa vez xD")
