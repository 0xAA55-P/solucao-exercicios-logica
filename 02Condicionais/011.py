"""
Descrição: Peça o peso e a altura do usuário, calcule o Índice de Massa Corporal (IMC) e classifique-o.

Explicação do Conceito:

IMC: É uma medida que relaciona peso e altura. A fórmula é: IMC = peso / (altura × altura).
Classificação:
Abaixo do peso: IMC < 18.5
Peso normal: 18.5 ≤ IMC < 25
Sobrepeso: 25 ≤ IMC < 30
Obesidade: IMC ≥ 30
"""

def main():
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))

  imc = peso / (altura ** 2)
  classificacao = None

  if imc < 18.5:
    classificacao = "Abaixo do peso"
  elif 18.5 <= imc <= 25:
    classificacao = "Peso normal"
  elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
  else:
    classificacao = "Obesidade"

  print(f"Classificação: {classificacao}")
  print(f"IMC: {imc:.1f}")

if __name__ == '__main__':
	main()
