# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random
a = "João"
b = "Pedro"
c = "Marcelo"
d = "Gabrielle"
conjunto = [a, b, c, d]
print("O aluno escolhido para apagar o quadro é {}".format(random.choice(conjunto)))
