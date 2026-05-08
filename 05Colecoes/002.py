"""
Descrição: Solicite ao usuário que insira as notas de 5 alunos e armazene-as em um vetor (ou array, ou lista). Calcule e exiba a média das notas.
"""

def main() -> None:
  notas: list[float] = []
  soma: float = 0
  media: float = 0

  for i in range(0, 5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

  for nota in notas:
    soma += nota

  print(f"A média das notas é: {soma / len(notas):.1f}")

if __name__ == '__main__':
	main()
