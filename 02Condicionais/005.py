"""
Descrição: Solicite a idade do usuário e informe se ele é menor ou maior de 18.
"""

def main():
  idade = int(input("Sua idade: "))

  if idade >= 18:
    print(f"Você é maior de idade")
  else:
    print(f"Você é menor de idade")

if __name__ == '__main__':
	main()
