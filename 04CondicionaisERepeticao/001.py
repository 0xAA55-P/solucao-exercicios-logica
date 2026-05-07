"""
Descrição: Apresente um menu com as opções:

Soma
Subtração
Multiplicação
Divisão
Sair Permita que o usuário escolha uma operação, insira dois números e exiba o resultado. O menu deve ser exibido novamente até que o usuário escolha sair.
"""

def main():
  while True:
    print("\n1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = int(input("\nEscolha uma opção: "))

    if escolha < 1 or escolha > 5:
      print("\nEscolha inválida, tente novamente.")
      continue

    if escolha == 5:
      break

    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = None

    match escolha:
      case 1:
        resultado = num1 + num2
      case 2:
        resultado = num1 - num2
      case 3:
        resultado = num1 * num2
      case 4:
        if num2 == 0:
          print("\nImpossivel dividir por 0.")
          resultado = "Inválido."
        else:
          resultado = num1 / num2

    print(f"Resultado: {resultado}")

if __name__ == '__main__':
	main()
