"""
Descrição: Leia dois conjuntos de números inteiros (cada um com 5 elementos) e exiba os números que estão presentes em ambos os conjuntos.

alternativa preenchendo os vetores usando a função randint
"""

import random

def main() -> None:
  c1: list[int] = [random.randint(1, 10) for _ in range(1, 100)]
  c2: list[int] = [random.randint(1, 10) for _ in range(1, 100)]
  presentes: list[int] = []
  

  for i in range(0, len(c1) - 1):
  #  for j in range(i, len(c1) - 1):
    if c1[i] == c2[i]:
      presentes.append(c1[i])

  print("Presentes em ambos os conjuntos:")
  for num in presentes:
    print(num, end=" ")
  print()

if __name__ == '__main__':
	main()
