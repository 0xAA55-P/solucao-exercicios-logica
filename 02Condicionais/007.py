"""
Descrição: Peça ao usuário um ano e determine se é um ano bissexto.

Explicação do Conceito: Um ano é bissexto se é divisível por 4, mas não por 100, exceto se for também divisível por 400.
"""

def main():
  ano = int(input("Digite o ano: "))

  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
  else:
    print(f"O ano {ano} não é bissexto")

if __name__ == '__main__':
	main()
