"""
Leia dois números e um operador matemático (+, -, *, /). Realize a operação indicada e mostre o resultado.
"""

def main():
  num1 = int(input("Primeiro numero: "))
  num2 = int(input("Segundo numero: "))
  operador = input("Operador (+, -, *, /): ")

  resultado = 0

  match operador:
    case "+":
      resultado = num1 + num2
    case "-":
      resultado = num1 - num2
    case "*":
      resultado = num1 * num2
    case "/":
      if num2 == 0:
        print("Impossivel dividir por 0.")
        resultado = "Indefinido"
      else:
        resultado = num1 / num2

    case _:
      print("Operador inválido!")
      resultado = "Indefinido"

  print(f"Resultado: {resultado}")

if __name__ == '__main__':
	main()
