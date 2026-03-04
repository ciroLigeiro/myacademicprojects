from datetime import datetime # Importa a classe datetime do módulo datetime

class Relatorio:  # Define a classe Relatorio
    
    def generate_report(tarefas, password_change_info=None):  # Define o método generate_report com parâmetros tarefas e password_change_info
        report = ""  # Uma string vazia para armazenar o relatório
        current_time = datetime.now().strftime("%Y-%m-%d")  # Obtém a data atual formatada como 'YYYY-MM-DD'
        for tarefa in tarefas: 
            report += f"{tarefa.title} - {tarefa.description} - {tarefa.category} - {current_time} - {tarefa.status} - {tarefa.user}\n"  # Adiciona informações da tarefa ao relatório
        if password_change_info:  # Verifica se há informações de alteração de senha
            report += f"Alteração de Senha: {password_change_info}\n"  # Adiciona informações de alteração de senha ao relatório
        return report  # Retorna o relatório gerado
    
    def save_report(report):  
        with open('relatorio.txt', 'a') as file:  # Abre o arquivo 'relatorio.txt' em modo de anexação
            file.write(report)  # Escreve o relatório no arquivo