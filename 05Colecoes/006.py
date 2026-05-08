"""
Descrição: Peça ao usuário que digite uma frase. Conte e exiba o número de caracteres (sem contar espaços) que a frase contém
"""

def main() -> None:
  frase: str = input("Digite uma frase: ")
  total = 0

  for char in frase:
    if char == ' ':
      continue

    total += 1

  print(f"A frase tem {total} caracteres")

if __name__ == '__main__':
	main()
