"""
Descrição: Leia um conjunto de números inteiros (quantidade definida pelo usuário) e armazene-os em um vetor. Calcule e exiba o valor máximo, mínimo e a média dos números.

soluçao sem max/min
"""

import random

def main() -> None:
  numeros: list[int] = [random.randint(1, 100) for _ in range(1, 50)]
  maior: int = numeros[0]
  menor: int = numeros[0]
  media: float = 0

  for num in numeros:
    if num > maior:
      maior = num

    if num < menor:
      menor = num

    media += num

  media /= len(numeros)

  print(f"Maior número: {maior} | Menor número: {menor} | Média: {media:.2f}")

if __name__ == '__main__':
	main()
