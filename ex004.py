# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

informacao = input('Digite algo')

print("A informação é um alfanumérico?", informacao.isalnum())
print("A informação é um alfabeto?", informacao.isalpha())
print("A informação é um treco?", informacao.isascii())
print("A informação é um digito?", informacao.isdigit())
print("A informação contém apenas letras minúsculas?", informacao.islower())
print("A informação é um decmal?", informacao.isdecimal())
print("A informação é um algo?", informacao.isidentifier())
print("A informação é um número?", informacao.isnumeric())
print("A informação é um printável?", informacao.isprintable())
print("A informação é um espaço?", informacao.isspace())
print("A informação é um título?", informacao.istitle())
print("A informação écontém apenas letras maiúsculas?", informacao.isupper())
