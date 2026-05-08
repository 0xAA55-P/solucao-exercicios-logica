"""
Descrição: Armazene uma lista de 5 nomes em um vetor (ou array, ou lista). Peça ao usuário que digite um nome e informe se esse nome está na lista.
"""

def main() -> None:
  nomes: list[str] = ["Anna", "Bruno", "Carlos", "Daniela", "Lucca"]
  nome_para_buscar: str = input("Nome para buscar: ").capitalize()

  if nome_para_buscar in nomes:
    print("O Nome está na lista")
  else:
    print("O Nome não está na lista")

if __name__ == '__main__':
	main()
