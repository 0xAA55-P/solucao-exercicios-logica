"""
Descrição: Exiba todos os números pares no intervalo de 1 a 50.
"""

def main():
  for i in range(1, 51):
    if i % 2 == 0:
      print(i, end=" ")

  print()

if __name__ == '__main__':
	main()
