"""
Descrição: Leia 5 números inteiros e armazene-os em um vetor (ou array, ou lista). Em seguida, calcule e exiba a soma desses números.
"""

def main() -> None:
  numeros: list[int] = []
  soma: float = 0

  for i in range(0, 5):
    num = int(input(f"Digite o {i + 1} número do array: "))
    numeros.append(num)

  for num in numeros:
    soma += num

  print(f"Soma dos elementos: {soma}")
    

if __name__ == '__main__':
	main()
