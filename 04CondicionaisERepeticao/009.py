"""
Jogo da Forca Simplificado

Descrição: Defina uma palavra secreta no código. O usuário deve tentar adivinhar as letras até completar a palavra ou atingir o número máximo de tentativas.
"""

import random
import re

PALAVRAS = [
    "exceto", "cínico", "idôneo", "âmbito", "néscio",
    "mister", "índole", "defina", "vereda", "apogeu",
    "inócuo", "convém", "escopo", "utopia", "sádico",
    "ênfase", "idiota", "alusão", "mérito", "hostil",
    "casual", "cético", "anseio", "legado", "gentil",
    "pressa", "hétero", "alheio", "paixão", "nocivo",
    "infame", "clichê", "afável", "exímio", "dádiva",
    "também", "êxtase", "adorno", "larica", "otário",
    "astuto", "aferir", "sóbrio", "adesão", "sessão",
    "glória", "solene", "limiar", "julgar", "ensejo",
    "embora"
]
PALAVRA_SECRETA = random.choice(PALAVRAS)

def main():
  tentativas = 12

  tamanho = len(PALAVRA_SECRETA)
  palavra_ofuscada = "_" * tamanho
  caracteres_tentados = []

  while tentativas != 0:
    print(f"Palavra secreta: {palavra_ofuscada}")
    chute = input("Chute um caractere: ")

    if chute in PALAVRA_SECRETA:
      indices = [match.start() for match in re.finditer(chute, PALAVRA_SECRETA)]
      for indice in indices:
        palavra_ofuscada = palavra_ofuscada[:indice] + chute + palavra_ofuscada[indice+1:] # adiciona o caractere em sua posição original

    if chute in caracteres_tentados:
      print("Você já tentou esse caractere.")
      tentativas += 1
    else:
      caracteres_tentados.append(chute)

    if palavra_ofuscada == PALAVRA_SECRETA:
      print(f"Acertou! A palavra era: {PALAVRA_SECRETA}")
      break

    tentativas -= 1
    print(f"Errou. Tentativas restantes: {tentativas}")

if __name__ == '__main__':
	main()
