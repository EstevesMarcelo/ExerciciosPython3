# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a = input("Indique o primeiro aluno para realizar a apresentação do trabalho hoje")
b = input("Indique outro aluno para realizar a apresentação do trabalho hoje")
c = input("Indique mais um aluno para realizar a apresentação do trabalho hoje")
d = input("Por fim, indique mais um aluno para realizar a apresentação do trabalho hoje")

conjunto = [a, b, c, d]
print("A ordem de apresentação é: {}".format(random.sample(conjunto, 4)))
