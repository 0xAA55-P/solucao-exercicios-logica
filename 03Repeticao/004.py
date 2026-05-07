"""
Descrição: Leia um número inteiro não negativo e calcule seu fatorial.

Explicação do Conceito: O fatorial de um número n (representado por n!) é o produto de todos os números inteiros positivos de 1 até n.
"""

def main():
  numero = int(input("Digite um numero inteiro positivo: "))
  fatorial = 1

  if numero < 0:
    print("o numero nao pode ser negativo.")
    exit()

  for i in range(1, numero + 1):
    fatorial *= i

  print(f"O fatorial de {numero} é {fatorial}")

if __name__ == '__main__':
	main()
