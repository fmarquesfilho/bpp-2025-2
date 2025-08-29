# Função com múltiplas responsabilidades
def processar_tarefas(tarefas):
    for tarefa in tarefas:
        if tarefa.status == "pendente":
            print("Descrição:", tarefa.descricao)
            enviar_email(tarefa.usuario.email)
            tarefa.status = "processado"
            salvar_banco(tarefa)