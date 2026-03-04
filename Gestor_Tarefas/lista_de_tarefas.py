from tarefa import Tarefa  # Importa a classe Tarefa do módulo tarefa

class ListaDeTarefas:  # Define a classe ListaDeTarefas que gerencia uma lista de tarefas
    def __init__(self, user):
        self.tarefas = []  
        self.user = user 
        self.load_tasks()  # Carrega as tarefas existentes do arquivo ao inicializar

    def add_task(self, task):  # Define um método para adicionar uma nova tarefa
        self.tarefas.append(task)  
        self.save_tasks()  # Guarda a lista de tarefas atualizada no arquivo

    def remove_task(self, task):  # Define um método para remover uma tarefa existente
        self.tarefas.remove(task)  
        self.save_tasks()

    def get_tasks(self):  # Define um método para obter as tarefas do utilizador atual
        return [tarefa for tarefa in self.tarefas if tarefa.user == self.user]

    def save_tasks(self):  # Define um método para salvar as tarefas em um arquivo
        with open('lista_de_tarefas.txt', 'w') as file:
            for tarefa in self.tarefas:
                file.write(str(tarefa) + "\n")

    def load_tasks(self):  # Define um método para carregar tarefas de um arquivo
        try:
            with open('lista_de_tarefas.txt', 'r') as file:  # Tenta abrir o arquivo para leitura
                for line in file:  
                    parts = line.strip().split(' - ') 
                    if len(parts) == 6:
                        title, description, category, creation_date, status, user = parts 
                        tarefa = Tarefa(title, description, category, user) 
                        tarefa.creation_date = creation_date
                        tarefa.status = status
                        self.tarefas.append(tarefa)  # Adiciona a tarefa à lista de tarefas
                    else:
                        print(f"Skipping invalid line: {line.strip()}")  # Ignora linhas inválidas
        except FileNotFoundError:  # Captura a exceção se o arquivo não for encontrado
            pass  # Não faz nada se o arquivo não existir