from datetime import datetime  # Importa a classe datetime para manipulação de datas e horas

class Tarefa:  # Define a classe Tarefa que representa uma tarefa
    def __init__(self, title, description, category, user):  # Inicia a tarefa com título, descrição, categoria e utilizador
        self.title = title  
        self.description = description  
        self.creation_date = datetime.now().strftime("%Y-%m-%d")  # Armazena a data de criação da tarefa no formato YYYY-MM-DD
        self.status = "Pendente" 
        self.category = category 
        self.user = user  

    def __str__(self):  # Define o método de string para representar a tarefa
        return f"{self.title} - {self.description} - {self.creation_date} - {self.status} - {self.category} - {self.user}"  # Retorna uma string formatada com os detalhes da tarefa

    def conclude(self): 
        self.status = "Concluída"  # Altera o status da tarefa para "Concluída"
