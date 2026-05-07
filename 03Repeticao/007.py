"""
Descrição: Continue solicitando ao usuário um número entre 1 e 10 até que ele forneça um valor nesse intervalo.
"""

def main():
  while (numero := int(input("Digite um numero entre 1-10: "))) > 10 or numero < 1:
    print("Numero inválido")

  print("Número válido.")

if __name__ == '__main__':
	main()
