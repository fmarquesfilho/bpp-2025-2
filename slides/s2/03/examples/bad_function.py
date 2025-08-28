# Função com múltiplas responsabilidades
def exibir_tarefas_incompletas(lista_de_tarefas):
    for tarefa in lista_de_tarefas:
        if not tarefa.completa:
            print("Tarefa:", tarefa.nome)
            print("Descrição:", tarefa.descricao)
            print("Prazo:", tarefa.prazo)
            print("-" * 30)
            