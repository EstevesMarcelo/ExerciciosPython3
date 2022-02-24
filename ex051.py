# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

# Solução particular
a0 = float(input("Digite o primeiro termo da sua PA:"))
r = float(input("Digite a razão da sua PA: "))
s = []
for i in range(0, 10):
    b = a0 + r*i
    s = s + [b]
print("Os 10 primeiros termos de sua PA são: {} .".format(s))

# Solução do Guanabara

primeiro = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10-1)*razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("Acabou")
