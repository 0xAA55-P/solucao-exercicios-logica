"""
Descrição: O programa escolhe um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número, e o programa dará dicas se o número é maior ou menor após cada tentativa. O jogo continua até que o usuário acerte.
"""

import random # gerar um numero

def gerar_numero() -> int:
  return random.randint(1, 101)

def main():
  numero_escolhido = gerar_numero()
  tentativas = 1

  print("Um numero entre 1 a 100 foi escolhido. Tente adivinhá-lo")

  while (chute := int(input("Digite seu chute: "))) != numero_escolhido:
    if chute > numero_escolhido:
      print("Muito alto! Tente novamente.")
    elif chute < numero_escolhido:
      print("Muito baixo! Tente novamente.")

    tentativas += 1

  print("Parabens! Você acertou.")
  print(f"Tentativas: {tentativas}")

if __name__ == '__main__':
	main()
