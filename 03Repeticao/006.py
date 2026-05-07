"""
Descrição: Peça um número N e exiba os N primeiros termos da sequência de Fibonacci.

Explicação do Conceito: A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores.
"""

def main():
  numero = int(input("Digite o numero: "))
  penultimo = 0
  ultimo = 1

  print("0 1", end=" ")

  for i in range(3, numero + 1):
    termo = ultimo + penultimo
    penultimo, ultimo = ultimo, termo
    print(termo, end=" ")

  print()

if __name__ == '__main__':
	main()
