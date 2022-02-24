#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior valor
# que estão na tupla.
import random
a= random.randint(0,9)
b=random.randint(0,9)
c=random.randint(0,9)
d=random.randint(0,9)
e = random.randint(0,9)

f = (a,b,c,d,e)
print('-'*30)
print(f'A listagem dos números é a seguinte: {f}')
print('-'*30)
print(f'O menor valor do conjunto é {min(f)}')
print('-'*30)
print(f'O maior valor do conjunto é {max(f)}')

