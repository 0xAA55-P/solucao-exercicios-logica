"""
Descrição: Leia 5 números inteiros, armazene-os em um vetor (ou array, ou lista) e exiba os números em ordem crescente usando o algoritmo Bubble Sort.

Explicação do Conceito: O Bubble Sort compara elementos adjacentes e os troca se estiverem fora de ordem. Este processo é repetido até que toda a lista esteja ordenada.
"""

import random

def main() -> None:
  """
  Para pedir os numeros, faça:

    numeros: list[int] = []

    for i in range(0, 5):
      numero = int(input(f"Digite o {i + 1}° Numero: "))
      numeros.append(numero)
  """

  # ou preencha com list comprehension
  numeros: list[int] = [random.randint(1, 100) for i in range(100)]

  tamanho: int = len(numeros)

  for i in range(0, tamanho - 1):
    for j in range(0, tamanho - 1 - i):
      if numeros[j] > numeros[j + 1]:
        numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

  print(numeros)

if __name__ == '__main__':
	main()
