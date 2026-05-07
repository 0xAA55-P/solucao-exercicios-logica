"""
Descrição: Leia a nota final de um aluno e informe se ele está aprovado (nota maior ou igual a 6) ou reprovado.
"""

def main():
  nota_final = float(input("Digite a nota final do aluno: "))

  resultado = "Aprovado" if nota_final >= 6 else "Reprovado"
  """
    ou tambem:

    if nota_final >= 6:
      resultado = "Aprovado"
    else:
      resultado = "Reprovado"
  """

  print(f"Resultado: {resultado}")

if __name__ == '__main__':
	main()
