class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def autenticar(self, email, senha):
        """Retorna se o login é válido para este usuário"""
        if self.email == email and self.senha == senha:
            print(f"✅ Autenticação bem-sucedida para {self.nome}!")
            return True
        else:
            print(f"❌ Falha na autenticação para {self.nome}!")
            return False
    
    def __str__(self):
        return f"Usuário: {self.nome} | Email: {self.email}"

# Teste direto conforme solicitado
print("=== TESTE DE AUTENTICAÇÃO DE USUÁRIOS ===\n")

# Criando dois usuários
usuario1 = Usuario("Maria Santos", "maria@email.com", "minhasenha123")
usuario2 = Usuario("João Silva", "joao@empresa.com", "senhasecreta")

print("Usuários criados:")
print(f"1. {usuario1}")
print(f"2. {usuario2}")

# Simulando logins corretos e incorretos
print("\n--- TESTES DE LOGIN ---")

print("\n1. Login correto do usuário 1:")
usuario1.autenticar("maria@email.com", "minhasenha123")

print("\n2. Login correto do usuário 2:")
usuario2.autenticar("joao@empresa.com", "senhasecreta")

print("\n3. Login incorreto - senha errada:")
usuario1.autenticar("maria@email.com", "senha_errada")

print("\n4. Login incorreto - email errado:")
usuario2.autenticar("email_errado@teste.com", "senhasecreta")

print("\n5. Credenciais trocadas entre usuários:")
usuario1.autenticar("joao@empresa.com", "senhasecreta")  # Email do 2, senha do 2
usuario2.autenticar("maria@email.com", "minhasenha123")  # Email do 1, senha do 1