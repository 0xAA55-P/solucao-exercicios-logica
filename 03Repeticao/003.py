"""
Descrição: Solicite um número inteiro positivo N e calcule a soma de todos os números de 1 até N.
"""

def main():
  numero = int(input("Digite um numero positivo: "))
  soma = 0

  if numero < 0:
    print("O número não pode ser negativo.")
    exit()

  for i in range(1, numero + 1):
    soma += i

  print(f"A soma de 1 até {numero} é: {soma}")

if __name__ == '__main__':
	main()
