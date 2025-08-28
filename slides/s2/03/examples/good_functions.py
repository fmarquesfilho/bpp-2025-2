# Funções especializadas e focadas
def exibir_tarefas_incompletas(tarefas):
    tarefas_incompletas = filtrar_tarefas_incompletas(tarefas)
    for tarefa in tarefas_incompletas:
        exibir_tarefa(tarefa)

def filtrar_tarefas_incompletas(tarefas):
    return [tarefa for tarefa in tarefas if not tarefa.completa]

def exibir_tarefa(tarefa):
    print(f"Tarefa: {tarefa.nome}")
    print(f"Descrição: {tarefa.descricao}")
    print(f"Prazo: {tarefa.prazo}")
    print("-" * 30)