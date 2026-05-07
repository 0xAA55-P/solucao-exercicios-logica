"""
Descrição: Com base na idade fornecida, classifique o nadador em uma das seguintes categorias:

Infantil: até 10 anos
Juvenil: 11 a 17 anos
Adulto: 18 anos ou mais
"""

def main():
  idade = int(input("Digite a idade do nadador: "))
  categoria = None

  if idade <= 10:
    categoria = "Infantil"
  elif 11 <= idade <= 17:
    categoria = "Juvenil"
  else:
    categoria = "Adulto"

  print(f"Categoria: {categoria}")

if __name__ == '__main__':
	main()
