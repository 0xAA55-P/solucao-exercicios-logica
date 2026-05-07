"""
Descrição: Peça um número inteiro e determine se ele é primo.

Explicação do Conceito: Um número primo é um número maior que 1 que é divisível apenas por 1 e por ele mesmo.
"""

def eh_primo(numero) -> bool:
  for i in range(2, numero):
    if numero % i == 0:
      return False # se o numero for divisivel por qualquer numero entre 2...numero, nao é primo

  return True

def main():
  numero = int(input("Digite um numero inteiro: "))

  if eh_primo(numero):
    print(f"O número {numero} é primo")
  else:
    print(f"O número {numero} não é primo")

if __name__ == '__main__':
	main()
