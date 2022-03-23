# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
n = float(input("Digite um número: "))
print(f'Aumentando {n} em 10%, temos como resultado {moeda.aumentar(n)}')
print(f'Diminuindo {n} em 10%, temos como resultado {moeda.diminuir(n)}')
print(f'Dobrando {n}, temos como resultado {moeda.dobro(n)}')
print(f'Dividindo {n} pela metade, temos como resultado {moeda.metade(n)}')
