"""
Descrição: Leia os comprimentos dos três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno.

Explicação do Conceito:

Equilátero: Todos os lados iguais.
Isósceles: Dois lados iguais.
Escaleno: Todos os lados diferentes.
"""

def main():
  lado1 = float(input("Comprimento do lado 1: "))
  lado2 = float(input("Comprimento do lado 2: "))
  lado3 = float(input("Comprimento do lado 3: "))

  resultado = None

  if lado1 == lado2 and lado1 == lado3:
    resultado = "Equilátero"
  elif lado1 == lado2 or lado2 == lado1 or lado2 == lado3 or lado3 == lado1 or lado3 == lado2:
    resultado = "Isósceles"
  else:
    resultado = "Escaleno"

  print(f"Resultado: {resultado}")
  
if __name__ == '__main__':
	main()
