"""
Descrição: Leia uma temperatura em graus Celsius e converta-a para Fahrenheit. A fórmula de conversão é: F = (C × 9/5) + 32.
"""

def main():
  celsius = float(input("Digite a temperatura em Celsius: "))
  fahrenheit = (celsius * 9 / 5) + 32

  print(f"A temperatura em Fahrenheit é: {fahrenheit}")

if __name__ == '__main__':
	main()
