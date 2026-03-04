from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QComboBox
from tarefa import Tarefa  #Importa a classe Tarefa que representa uma tarefa
from relatorio import Relatorio  #Importa a classe Relatorio para gerar relatórios de tarefas
from lista_de_tarefas import ListaDeTarefas  #Importa a classe ListaDeTarefas que gerencia as tarefas de um utilizador
from sistema_gestao_tarefas import SistemaGestaoTarefas  #Importa a classe SistemaGestaoTarefas que gerencia utilizadores e autenticação
  
class AppWindow(QWidget): #Classe principal da janela de login
    def __init__(self, sistema_gestao_tarefas):
        super().__init__()
        self.sistema_gestao_tarefas = sistema_gestao_tarefas
        self.initUI()

    def initUI(self):  # Método para configurar a interface do utilizador
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 150)
        self.layout = QVBoxLayout()

        self.username_input = QLineEdit(self) # Campo de entrada para o nome do utilizador
        self.username_input.setPlaceholderText('Nome de Utilizador ')
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self) # Campo de entrada para a senha
        self.password_input.setPlaceholderText('Senha')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login', self) # Botão para realizar login
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.register_button = QPushButton('Registrar Novo Utilizador', self) # Botão para registrar um novo utilizador
        self.register_button.clicked.connect(self.open_registration)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def login(self): # Método para autenticar o utilizador
        username = self.username_input.text()
        password = self.password_input.text()
        if self.sistema_gestao_tarefas.authenticate_user(username, password):
            self.task_manager = Gestordetarefas(self.sistema_gestao_tarefas, username)
            self.task_manager.show()
            self.close() # Fecha a janela de login
        else:
            QMessageBox.warning(self, 'Erro', 'Nome de utilizador ou senha inválidos.') # Exibe mensagem de erro

    def open_registration(self): # Método para abrir a janela de registro
        self.registration_window = JanelaSignUp(self.sistema_gestao_tarefas)
        self.registration_window.show()

class JanelaSignUp(QWidget): # Classe para a janela de registro de novo utilizador
    def __init__(self, sistema_gestao_tarefas):
        super().__init__()
        self.sistema_gestao_tarefas = sistema_gestao_tarefas
        self.initUI()

    def initUI(self): #Método para configurar a interface do utilizador
        self.setWindowTitle('Registrar Novo Utilizador')
        self.setGeometry(100, 100, 300, 250)# Define a posição e o tamanho da janela

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit(self) # Campo de entrada para o nome
        self.name_input.setPlaceholderText('Nome')
        self.layout.addWidget(self.name_input)

        self.username_input = QLineEdit(self) # Campo de entrada para o username
        self.username_input.setPlaceholderText('Nome de Utilizador')
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self) # Campo de entrada para a senha
        self.password_input.setPlaceholderText('Senha')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.register_button = QPushButton('Registrar', self) # Botão para registrar o utilizador
        self.register_button.clicked.connect(self.register_user)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def register_user(self):  # Método para registrar um novo utilizador
        name = self.name_input.text()  # Obtém o nome digitado
        username = self.username_input.text()  # Obtém o username digitado
        password = self.password_input.text()  # Obtém a senha digitada
        if name and username and password:  # Verifica se todos os campos estão preenchidos
            if username not in self.sistema_gestao_tarefas.utilizadores:  # Verifica se o nome de utilizador já existe
                self.sistema_gestao_tarefas.add_user(username, password, name)  # Adiciona o novo utilizador ao sistema
                QMessageBox.information(self, 'Sucesso', 'Utilizador registrado com sucesso!')  # Exibe mensagem de sucesso
                self.close()  # Fecha a janela de registro
            else:
                QMessageBox.warning(self, 'Erro', 'Nome de utilizador já existe.')  # Exibe mensagem de erro
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos.')  # Exibe mensagem de erro


class JanelaAlterarPalavraPasse(QWidget):  # Classe para a janela de alteração de senha
    def __init__(self, sistema_gestao_tarefas, username):
        super().__init__()
        self.sistema_gestao_tarefas = sistema_gestao_tarefas
        self.username = username
        self.initUI()

    def initUI(self):  # Método para configurar a interface do utilizador
        self.setWindowTitle('Alterar Palavra-Passe')
        self.setGeometry(100, 100, 400, 150)
        self.layout = QVBoxLayout()

        self.new_password_input = QLineEdit(self) # Campo de entrada para a nova senha
        self.new_password_input.setPlaceholderText('Nova Senha')
        self.new_password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.new_password_input)

        self.change_password_button = QPushButton('Alterar Palavra-Passe', self)  # Botão para alterar a senha
        self.change_password_button.clicked.connect(self.change_password)
        self.layout.addWidget(self.change_password_button)

        self.setLayout(self.layout)

    def __init__(self, sistema_gestao_tarefas, username): 
        super().__init__()
        self.sistema_gestao_tarefas = sistema_gestao_tarefas
        self.username = username  # Armazena o nome de utilizador logado
        self.initUI()

    def change_password(self):  # Método para alterar a senha
        new_password = self.new_password_input.text()  # Obtém a nova senha digitada
        if new_password:  # Verifica se a nova senha foi preenchida
            if self.sistema_gestao_tarefas.change_password(self.username, new_password):  # Tenta alterar a senha
                QMessageBox.information(self, 'Sucesso', 'Palavra passe alterada com sucesso!')  # Exibe mensagem de sucesso
                self.close()  # Fecha a janela de alteração de senha
            else:
                QMessageBox.warning(self, 'Erro', 'Nome de utilizador não encontrado.')  # Exibe mensagem de erro
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos.')  # Exibe mensagem de erro

class Gestordetarefas(QWidget):  # Classe para a janela do gestor de tarefas
    def __init__(self, sistema_gestao_tarefas, username):
        super().__init__()
        self.sistema_gestao_tarefas = sistema_gestao_tarefas
        self.lista_de_tarefas = ListaDeTarefas(username)
        self.initUI()

    def initUI(self):  # Método para configurar a interface do utilizador
        self.setWindowTitle('Gestor de Tarefas')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.task_list_widget = QListWidget(self)  # Widget para exibir a lista de tarefas
        self.layout.addWidget(self.task_list_widget)  # Adiciona o widget ao layout

        self.title_input = QLineEdit(self)  # Campo de entrada para o título da tarefa
        self.title_input.setPlaceholderText('Título da Tarefa')  
        self.layout.addWidget(self.title_input)  # Adiciona o campo ao layout

        self.description_input = QLineEdit(self)  # Campo de entrada para a descrição da tarefa
        self.description_input.setPlaceholderText('Descrição da Tarefa')  
        self.layout.addWidget(self.description_input) 

        self.category_input = QComboBox(self)  # ComboBox para selecionar a categoria da tarefa
        self.category_input.addItems(['Trabalho', 'Pessoal', 'Estudos'])  # Adiciona categorias
        self.layout.addWidget(self.category_input)  

        self.add_task_button = QPushButton('Adicionar Tarefa', self)  # Botão para adicionar uma nova tarefa
        self.add_task_button.clicked.connect(self.add_task)  # Conecta o clique do botão à função de adicionar tarefa
        self.layout.addWidget(self.add_task_button)  

        self.remove_task_button = QPushButton('Remover Tarefa', self)  # Botão para remover uma tarefa selecionada
        self.remove_task_button.clicked.connect(self.remove_task)  # Conecta o clique do botão à função de remover tarefa
        self.layout.addWidget(self.remove_task_button)  

        self.conclude_task_button = QPushButton('Concluir Tarefa', self)  # Botão para marcar uma tarefa como concluída
        self.conclude_task_button.clicked.connect(self.conclude_task)  # Conecta o clique do botão à função de concluir tarefa
        self.layout.addWidget(self.conclude_task_button)  
        
        self.logout_button = QPushButton('Logout', self)  # Botão para logout
        self.logout_button.clicked.connect(self.logout)
        self.layout.addWidget(self.logout_button)

        # Filtros
        self.category_filter = QComboBox(self)  # ComboBox para filtrar tarefas por categoria
        self.category_filter.addItems(['Todas', 'Trabalho', 'Pessoal', 'Estudos'])  # Adiciona opções de filtro
        self.layout.addWidget(self.category_filter)  # Adiciona o ComboBox ao layout

        self.status_filter = QComboBox(self)  # ComboBox para filtrar tarefas por status
        self.status_filter.addItems(['Todos', 'Pendente', 'Concluída'])  # Adiciona opções de filtro
        self.layout.addWidget(self.status_filter) 

        self.filter_button = QPushButton('Filtrar Tarefas', self)  # Botão para aplicar filtros nas tarefas
        self.filter_button.clicked.connect(self.filter_tasks)  # Conecta o clique do botão à função de filtrar tarefas
        self.layout.addWidget(self.filter_button) 
        
        self.change_password_button = QPushButton('Alterar Senha', self)  # Botão para abrir a janela de alteração de senha
        self.change_password_button.clicked.connect(self.open_change_password_window)  # Conecta o clique do botão à função de abrir a janela de alteração de senha
        self.layout.addWidget(self.change_password_button)  

        self.generate_report_button = QPushButton('Gerar Relatório', self)  # Botão para gerar um relatório das tarefas
        self.generate_report_button.clicked.connect(self.generate_report)  # Conecta o clique do botão à função de gerar relatório
        self.layout.addWidget(self.generate_report_button)  

        self.setLayout(self.layout)
        self.load_tasks_to_widget()

    def load_tasks_to_widget(self):  # Método para carregar tarefas na lista de tarefas
        self.task_list_widget.clear()  # Limpa a lista atual
        for tarefa in self.lista_de_tarefas.get_tasks():
            self.task_list_widget.addItem(str(tarefa)) # Adiciona cada tarefa à lista

    def add_task(self):  # Método para adicionar uma nova tarefa
        title = self.title_input.text()  # Obtém o título da tarefa
        description = self.description_input.text()  # Obtém a descrição da tarefa
        category = self.category_input.currentText()  # Obtém a categoria selecionada
        if title and description:  # Verifica se o título e a descrição estão preenchidos
            new_task = Tarefa(title, description, category, self.lista_de_tarefas.user)  # Cria uma nova tarefa
            self.lista_de_tarefas.add_task(new_task)  # Adiciona a nova tarefa à lista de tarefas
            self.load_tasks_to_widget()  # Atualiza a lista de tarefas
            self.title_input.clear()  # Limpa o campo de título
            self.description_input.clear()  # Limpa o campo de descrição
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos.')

    def remove_task(self):
        selected_item = self.task_list_widget.currentItem() # Obtém a tarefa selecionada
        if selected_item:
            task_to_remove = next((task for task in self.lista_de_tarefas.get_tasks() if str(task) == selected_item.text()), None) # Encontra a tarefa correspondente
            if task_to_remove:
                self.lista_de_tarefas.remove_task(task_to_remove) # Remove a tarefa da lista
                self.load_tasks_to_widget()  # Atualiza a lista de tarefas
        else:
            QMessageBox.warning(self, 'Erro', 'Selecione uma tarefa para remover.')

    def conclude_task(self): # Método para marcar uma tarefa como concluída
        selected_item = self.task_list_widget.currentItem() # Obtém a tarefa selecionada
        if selected_item:
            task_to_conclude = next((task for task in self.lista_de_tarefas.get_tasks() if str(task) == selected_item.text()), None) # Encontra a tarefa correspondente
            if task_to_conclude:
                task_to_conclude.conclude()
                self.lista_de_tarefas.save_tasks() # Guarda as tarefas atualizadas
                self.load_tasks_to_widget()  # Atualiza a lista de tarefas
        else:
            QMessageBox.warning(self, 'Erro', 'Selecione uma tarefa para concluir.')

    def filter_tasks(self): # Método para filtrar tarefas
        selected_category = self.category_filter.currentText()
        selected_status = self.status_filter.currentText() # Obtém o status selecionado

        self .task_list_widget.clear()  # Limpa a lista atual

        for tarefa in self.lista_de_tarefas.get_tasks():
            if selected_category != 'Todas' and tarefa.category != selected_category: # Filtra por categoria
                continue
            
            if selected_status == 'Pendente' and tarefa.status != 'Pendente':   # Filtra por status
                continue
            elif selected_status == 'Concluída' and tarefa.status != 'Concluída':
                continue
            
            self.task_list_widget.addItem(str(tarefa))   # Adiciona a tarefa filtrada à lista

    def open_change_password_window(self):
        self.change_password_window = JanelaAlterarPalavraPasse(self.sistema_gestao_tarefas, self.lista_de_tarefas.user)
        self.change_password_window.show()
    
    def generate_report(self):  # Método para gerar um relatório das tarefas
        selected_category = self.category_filter.currentText()
        selected_status = self.status_filter.currentText()

        # Filtrar tarefas com base nos critérios selecionados
        filtered_tasks = []
        for tarefa in self.lista_de_tarefas.get_tasks():
            if selected_category != 'Todas' and tarefa.category != selected_category: # Filtra por categoria
                continue
            if selected_status == 'Pendente' and tarefa.status != 'Pendente': # Filtra por status
                continue
            elif selected_status == 'Concluída' and tarefa.status != 'Concluída':
                continue
            filtered_tasks.append(tarefa) # Adiciona a tarefa filtrada à lista

        report = Relatorio.generate_report(filtered_tasks, self.sistema_gestao_tarefas.password_change_info)  #Gerar relatório apenas com as tarefas filtradas
        if report: # Verifica se o relatório foi gerado
            Relatorio.save_report(report) # Guarda o relatório em um arquivo
            report_dialog = QMessageBox(self) # Cria uma caixa de diálogo para exibir o relatório
            report_dialog.setWindowTitle('Relatório de Tarefas')
            report_dialog.setText(report) # Define o texto do relatório
            report_dialog.exec_()
        else:
            QMessageBox.warning(self, 'Erro', 'Não há tarefas para gerar relatório.') # Exibe mensagem de erro se não houver tarefas
    def logout(self):
        self.close()  # Fecha a janela do gestor de tarefas
        self.login_window = AppWindow(self.sistema_gestao_tarefas)  # Reabre a janela de login
        self.login_window.show()