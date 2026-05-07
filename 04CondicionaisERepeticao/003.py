"""
Descrição: Peça ao usuário para inserir as notas de vários alunos. O usuário deve indicar quando não há mais notas a serem inseridas. Calcule e exiba a média das notas inseridas.
"""

def main():
  soma = 0
  media = 0
  total_notas = 0

  while (nota := float(input("Digite a nota do aluno (-1 para sair): "))) != -1:
    soma += nota
    total_notas += 1

  media = soma / total_notas

  print(f"A média das notas é: {media:.2f}")

if __name__ == '__main__':
	main()
