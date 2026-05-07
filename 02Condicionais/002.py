"""
Descrição: Peça dois números ao usuário e exiba o maior deles.
"""

def main():
  num1 = int(input("Primeiro numero: "))
  num2 = int(input("Segundo numero: "))

  if num1 > num2:
    print(f"{num1} é o maior número")
  elif num1 < num2:
    print(f"{num2} é o maior número")
  else:
    print(f"Os números {num1} e {num2} são iguais.")

if __name__ == '__main__':
	main()
