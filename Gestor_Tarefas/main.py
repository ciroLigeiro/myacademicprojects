import sys  # Importa o módulo sys para manipulação de argumentos do sistema
from PyQt5.QtWidgets import QApplication  # Importa a classe QApplication do PyQt5 para criar a aplicação
from sistema_gestao_tarefas import SistemaGestaoTarefas  # Importa a classe SistemaGestaoTarefas que gerencia as tarefas
from interface import AppWindow  # Importa a classe AppWindow que representa a interface gráfica da aplicação

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente
    app = QApplication(sys.argv) 
    sistema_gestao_tarefas = SistemaGestaoTarefas()
    login_window = AppWindow(sistema_gestao_tarefas)  
    login_window.show()  
    sys.exit(app.exec_())  # Inicia o loop da aplicação e garante que o programa termine corretamente ao fechar