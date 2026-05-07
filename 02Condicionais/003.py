"""
Peça três números ao usuário e exiba o maior deles.
"""

def main():
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))
  num3 = int(input("Digite o terceiro numero: "))

  maior = 0

  if num1 >= num2 and num1 >= num3:
    maior = num1
  elif num2 >= num1 and num2 >= num3:
    maior = num2
  elif num3 >= num1 and num3 >= num1:
    maior = num3

  # valor inicial de maior é 0, se nenhuma das condições acima atender, permanece em 0 então são iguais.
  if maior == 0:
    print(f"Os números {num1}, {num2} e {num3} são iguais.")
  else:
    print(f"{maior} é o maior número")

if __name__ == '__main__':
	main()
