import hashlib  # Importa o módulo hashlib para realizar operações de hash

def hash_password(password):  # Define uma função para hash de senhas
    return hashlib.sha256(password.encode()).hexdigest()  # Retorna o hash SHA-256 da senha codificada

class Utilizador:  # Define a classe Utilizador que representa um utilizador do sistema
    def __init__(self, username, password, name):
        self.username = username 
        self.password = hash_password(password)  # Armazena a senha como um hash para segurança
        self.name = name  # Armazena o nome do utilizador