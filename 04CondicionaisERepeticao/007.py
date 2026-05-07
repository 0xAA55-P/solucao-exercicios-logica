"""
Descrição: Leia as notas dos alunos e atribua conceitos de acordo com a média:

A: 9 a 10
B: 7 a 8.9
C: 5 a 6.9
D: abaixo de 5
O programa deve continuar até que o usuário decida sair.
"""

def main():
  while True:
    nota = float(input("Digite a nota: "))
    conceito = None

    if nota > 10:
      print("A nota não pode ser maior que 10.")
      continue

    if nota >= 9 and nota <= 10:
      conceito = "A"
    elif nota >= 7 and nota <= 8.9:
      conceito = "B"
    elif nota >= 5 and nota <= 6.9:
      conceito = "C"
    else:
      conceito = "D"

    print(f"Conceito: {conceito}")

    continuar = input("Deseja continuar (S/N)? ").upper()

    if continuar == "N":
      break
    else:
      continue

if __name__ == '__main__':
	main()
