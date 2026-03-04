import hashlib # Importa o módulo hashlib para realizar operações de hash

def hash_password(password):  # Define uma função para hash de senhas
    return hashlib.sha256(password.encode()).hexdigest()  # Retorna o hash SHA-256 da senha codificada

class SistemaGestaoTarefas:  # Define a classe SistemaGestaoTarefas que gere utilizadores e as suas tarefas
    def __init__(self):
        self.utilizadores = {}  # Dicionário para armazenar utilizadores com os seus dados
        self.password_change_info = None  
        self.load_users()  

    def add_user(self, username, password, name):  # Método para adicionar um novo utilizador
        self.utilizadores[username] = {  
            'password': hash_password(password), 
            'name': name  # Armazena o nome do utilizador
        }
        self.save_users()  

    def save_users(self):  # Método para guardar os utilizadores em um arquivo
        with open('utilizadores.txt', 'w') as file:  
            for username, user_info in self.utilizadores.items():  # I
                file.write(f"{user_info['name']}_{username}:{user_info['password']}\n")  # Escreve os dados do utlizador no formato especificado

    def load_users(self):  # Método para carregar utilizadores de um arquivo
        try:
            with open('utilizadores.txt', 'r') as file:  # Abre o arquivo para leitura
                for line in file:  
                    if line.strip():
                        parts = line.strip().split(':')  # Divide a linha em partes usando ':' como delimitador
                        if len(parts) == 2:  # Verifica se há exatamente 2 partes
                            name_username, hashed_password = parts  # Desempacota as partes
                            if '_' in name_username:  # Verifica se o caractere '_' está presente
                                name, username = name_username.split('_')  # Separa nome e username
                                self.utilizadores[username] = {'password': hashed_password, 'name': name}  # Adiciona o utilizadores ao dicionário
                            else:
                                print(f"Formato inválido na linha: {line.strip()} - Esperado: 'nome_username:senha'")  # Mensagem de erro para formato inválido
                        else:
                            print(f"Formato inválido na linha: {line.strip()} - Esperado: 'nome_username:senha'")  # Mensagem de erro para formato inválido
        except FileNotFoundError:  
            print("Arquivo 'utilizadores.txt' não encontrado.")  

    def authenticate_user(self, username, password): 
        hashed_password = hash_password(password) 
        return self.utilizadores.get(username, {}).get('password') == hashed_password 

    def change_password(self, username, new_password):  # Método para alterar a senha de um utilizador
        if username in self.utilizadores:
            self.utilizadores[username]['password'] = hash_password(new_password)  
            self.password_change_info = f"Utilizador: {username} alterou a senha."  # Atualiza a informação sobre a alteração de senha
            self.save_users()  
            return True  # Retorna True indicando que a alteração foi bem-sucedida
        return False  