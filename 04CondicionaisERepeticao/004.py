"""
Descrição: Peça o capital inicial, a taxa de juros mensal e o número de meses. Calcule e exiba o montante final usando juros compostos.
Explicação do Conceito: Juros compostos são calculados sobre o capital inicial mais os juros acumulados. A fórmula é: Montante = Capital × (1 + Taxa)^Tempo.
"""

def main():
  capital_inicial = float(input("Capital inicial: "))
  taxa_mensal = int(input("Taxa de juros mensal (%): "))
  numero_de_meses = int(input("Número de meses: "))

  montante = capital_inicial * (1 + taxa_mensal / 100) ** numero_de_meses

  print(f"O montante após {numero_de_meses} é: {montante:.2f}")

if __name__ == '__main__':
	main()
