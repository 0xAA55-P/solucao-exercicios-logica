"""
Descrição: Permita que o usuário adicione ou remova itens de um estoque. Exiba a quantidade atual em estoque após cada operação. O programa deve continuar até que o usuário escolha sair.
"""

def main():
  itens_em_estoque = 0

  while True:
    print("\n1. Adicionar itens")
    print("2. Remover itens")
    print("3. Sair\n")

    escolha = int(input("Digite a escolha: "))

    if escolha < 1 or escolha > 3:
      print("Opção inválida.")
      continue

    if escolha == 3:
      break

    match escolha:
      case 1:
        quantidade_adicionar = int(input("Quantidade para adicionar: "))

        itens_em_estoque += quantidade_adicionar

      case 2:
        quantidade_remover = int(input("Quantidade para remover: "))
        itens_em_estoque -= quantidade_remover

    print(f"Quantidade em estoque: {itens_em_estoque}")

if __name__ == '__main__':
	main()
