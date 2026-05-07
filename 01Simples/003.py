"""
Descrição: Solicite o raio de um círculo e calcule a área. Use a fórmula: Área = π × raio². Considere π = 3.14159.
"""

def main():
  raio = float(input("Digite o raio do circulo: "))
  area = 3.14159 * raio ** 2

  print(f"A area do circulo é: {area}")

if __name__ == '__main__':
	main()
