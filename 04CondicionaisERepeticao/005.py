"""
Descrição: Simule um sistema de controle de abastecimento em um posto de gasolina. O programa deve permitir registrar vários abastecimentos, calculando o total de litros e o valor total a pagar. O loop deve continuar até que o usuário decida encerrar.
"""

def main():
  while True:
    litros_abastecidos = int(input("Digite a quantidade de litros abastecidos: "))
    preco_por_litro = float(input("Digite o preço por litro: "))

    valor_a_pagar = litros_abastecidos * preco_por_litro
    print(f"Valor a pagar: {valor_a_pagar:.2f}")

    repetir = input("Deseja registrar outro abastecimento? (S/N): ").upper()

    if repetir == 'N':
      break
    else:
      continue

if __name__ == '__main__':
	main()
