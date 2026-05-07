"""
Descrição: Peça um número inteiro e exiba a tabuada desse número de 1 a 10.
"""

def main():
  numero = int(input("Digite o numero para ver sua tabuada: "))

  print(f"Tabuada do {numero}:")

  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

if __name__ == '__main__':
	main()
