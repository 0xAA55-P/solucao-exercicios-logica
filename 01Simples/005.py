"""
Descrição: Peça o preço original de um produto e a porcentagem de desconto. Calcule e mostre o preço final após o desconto.
"""

def main():
  preco_original = float(input("Preço do produto: "))
  porcentagem_desconto = float(input("Porcentagem do desconto: "))

  preco_com_desconto = preco_original - (preco_original * porcentagem_desconto / 100)

  print(f"O preço com desconto é: {preco_com_desconto}")

if __name__ == '__main__':
	main()
