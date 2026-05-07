"""
Descrição: Solicite ao usuário um nome de usuário e senha. Dê até três tentativas para acertar. Se errar três vezes, exiba uma mensagem de conta bloqueada.
"""

NOME = "anna"
SENHA = "senhasegura123"

def main():
  tentativas = 1

  while True:
    nome_login = input("Nome de usuario: ")
    senha_login = input("Senha: ")

    if nome_login == NOME and senha_login == SENHA:
      print("Acesso permitido.")
      break
    else:
      print("Acesso negado.")
      print(f"Tentativas: {tentativas}")

    if tentativas == 3:
      print("Conta bloqueada.")
      break

    tentativas += 1

if __name__ == '__main__':
	main()
