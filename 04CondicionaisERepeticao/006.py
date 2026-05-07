"""
Descrição: Peça ao usuário um CPF (somente números) e verifique se ele tem 11 dígitos. Continue solicitando até que um CPF válido seja inserido.
"""

def main():
  while (len(input("Digite seu cpf (apenas numeros): "))) != 11:
    print("CPF Inválido.")

  print("CPF Válido.")

if __name__ == '__main__':
	main()
