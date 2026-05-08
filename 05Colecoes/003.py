"""
Descrição: Leia 10 números inteiros e armazene-os em um vetor (ou array, ou lista). Determine e exiba quantos números são pares.
"""

def main() -> None:
  numeros: list[int] = []
  total_pares = 0

  for i in range(0, 10):
    numero = int(input(f"Digite o {i + 1}° Numero: "))
    numeros.append(numero)

  for numero in numeros:
    if numero % 2 == 0:
      total_pares += 1

  print(f"A lista tem {total_pares} numeros pares.")

if __name__ == '__main__':
	main()
