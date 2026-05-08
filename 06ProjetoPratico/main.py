"""
Crie um programa que ajude o usuário a gerenciar suas tarefas diárias. O sistema permitirá adicionar, visualizar e marcar tarefas como concluídas. O objetivo é construir uma aplicação simples que agregue funcionalidades progressivamente.
"""

def main() -> None:
  tarefas: list[str] = []

  while True:
    print("\n1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Marcar Como Concluida")
    print("5. Sair")

    escolha = int(input("\nDigite a opção: "))

    if escolha < 1 or escolha > 5:
      print("\nEscolha inválida.")
      continue

    if escolha == 5:
      break

    match escolha:
      case 1:
        nome: str = input("\nNome da tarefa: ")
        adicionar_tarefa(tarefas, nome)
        print("\nTarefa adicionada.")

      case 2:
        listar_tarefas(tarefas)
        indice = int(input("\nIndice da tarefa para remover: "))

        remover_tarefa(tarefas, indice)
        print("\nTarefa removida.")

      case 3:
        listar_tarefas(tarefas)

      case 4:
        listar_tarefas(tarefas)
        indice = int(input("\nIndice da tarefa para marcar: "))
        marcar_como_completa(tarefas, indice)

def adicionar_tarefa(tarefas: list[str], nome: str) -> None:
  tarefa = "[ ] " + nome
  tarefas.append(tarefa)

def remover_tarefa(tarefas: list[str], indice: int) -> None:
  tarefas.pop(indice - 1)
  
def listar_tarefas(tarefas: list[str]) -> None:
  print()

  # 2 flags para evitar printar o header 2 vezes ou +
  mostrou_pendentes: bool = False
  mostrou_completas: bool = False
  
  for i, tarefa in enumerate(tarefas):
    if "[ ]" in tarefa:
      if not mostrou_pendentes:
        print("--- Pendentes:")
        mostrou_pendentes = True
      print(f"{i+1}. {tarefa}")

  for i, tarefa in enumerate(tarefas):
    if "[X]" in tarefa:
      if not mostrou_completas:
        print("--- Completas:")
        mostrou_completas = True
      print(f"{i+1}. {tarefa}")

def marcar_como_completa(tarefas: list[str], indice: int) -> None:
  tarefas[indice - 1] = tarefas[indice - 1].replace("[ ]", "[X]")

if __name__ == '__main__':
	main()
