# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
# como um valor monetário formatado.

import moeda
n = float(input("Digite um número: "))
print(f'Aumentando {moeda.moeda(n)} em 10%, temos como resultado {moeda.moeda(moeda.aumentar(n))}')
print(f'Diminuindo {moeda.moeda(n)} em 10%, temos como resultado {moeda.moeda(moeda.diminuir(n))}')
print(f'Dobrando {moeda.moeda(n)}, temos como resultado {moeda.moeda(moeda.dobro(n))}')
print(f'Dividindo {moeda.moeda(n)} pela metade, temos como resultado {moeda.moeda(moeda.metade(n))}')
