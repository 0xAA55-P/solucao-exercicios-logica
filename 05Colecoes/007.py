"""
Descrição: Leia uma palavra e conte quantas vezes cada letra aparece nela. Exiba o resultado para cada letra encontrada.
"""

def main() -> None:
  ocorrencias = {}
  palavra: str = input("Palavra: ")

  for char in palavra:
    if char == ' ':
      continue
    ocorrencias[char] = ocorrencias.get(char, 0) + 1

  for key, value in ocorrencias.items():
    print(f"{key}: {value}")

if __name__ == '__main__':
	main()
