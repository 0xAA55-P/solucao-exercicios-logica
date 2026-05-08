"""
Descrição: Leia 5 números e armazene-os em um vetor (ou array, ou lista). Exiba os números na ordem inversa à de entrada.
"""

import random

def main() -> None:
  numeros = [random.randint(1, 100) for _ in range(1, 11)]

  print("--- ordem padrao")
  for num in numeros:
    print(num, end=" ")

  print("\n--- invertida")
  reverse = numeros[::-1]
  for num in reverse:
    print(num, end=" ")
  print()

if __name__ == '__main__':
	main()
