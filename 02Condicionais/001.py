"""
Descrição: Leia um número inteiro e informe se ele é par ou ímpar.
"""

def main():
  numero = int(input("Digite um numero: "))

  if numero % 2 == 0:
    print("O numero é par")
  else:
    print("O numero é impar")

if __name__ == '__main__':
	main()
