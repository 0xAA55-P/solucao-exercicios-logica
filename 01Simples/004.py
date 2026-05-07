"""
Leia uma quantidade de dias e converta esse valor para o total de minutos.
"""

def main():
  quantidade_de_dias = float(input("Total de dias: "))
  minutos_no_dia = 60 * 24
  total_em_minutos = quantidade_de_dias * minutos_no_dia

  print(f"O total em minutos é: {total_em_minutos}")

if __name__ == '__main__':
	main()
