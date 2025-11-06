# Funções especializadas e focadas

def filtrar_tarefas_pendentes(tarefas):
    return [t for t in tarefas if t.status == "pendente"]

def notificar_usuario(tarefa):
    enviar_email(tarefa.usuario.email)

def exibir_tarefa(tarefa):
    print(f"Descrição: {tarefa.descricao}")

def atualizar_status_tarefa(tarefa):
    tarefa.status = "processado"
    salvar_banco(tarefa)

def processar_tarefas(tarefas):
    tarefas_pendentes = filtrar_tarefas_pendentes(tarefas)
    for tarefa in tarefas_pendentes:
        exibir_tarefa(tarefa)
        notificar_usuario(tarefa)
        atualizar_status_tarefa(tarefa)