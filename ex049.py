# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,só que agora utilizando um laço
# for.

print("\033[36mCalculadora para tabuada\033[m")
print()
print("-=-"*20)
a = int(input("Digite um número: "))
print("A tabuada de {} é:".format(a))
for i in range(1, 11):
    print("{} x {} = {}".format(a, i, a*i))
print()
print("-=-"*20)
print()
print("Tabuada finalizada")
