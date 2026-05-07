"""
Descrição: Solicite que o usuário insira uma senha. Se a senha estiver correta (defina você mesmo(a) uma senha padrão, como senha123), exiba "Acesso Permitido"; caso contrário, "Acesso Negado".
"""

SENHA = "senhasupersegura123"

def main():
  senha_usuario = input("Digite a senha: ")

  acesso = "Permitido" if senha_usuario == SENHA else "Negado"

  """
    ou tambem:

    if senha_usuario == SENHA:
      acesso = "Permitido"
    else:
      acesso = "Negado"
  """

  print(f"Acesso {acesso}")

if __name__ == '__main__':
	main()
