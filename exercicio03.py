class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha  # Em um sistema real, isso seria hash!
        self.ativo = True
    
    def autenticar(self, email, senha):
        """Verifica se o email e senha correspondem a este usuário"""
        if not self.ativo:
            print(f"❌ Usuário {self.nome} está inativo!")
            return False
        
        if self.email == email and self.senha == senha:
            print(f"✅ Login bem-sucedido! Bem-vindo(a), {self.nome}!")
            return True
        else:
            print(f"❌ Credenciais incorretas para {self.nome}!")
            return False
    
    def alterar_senha(self, senha_atual, nova_senha):
        """Permite ao usuário alterar sua própria senha"""
        if self.senha == senha_atual:
            self.senha = nova_senha
            print(f"✅ Senha alterada com sucesso para {self.nome}!")
            return True
        else:
            print(f"❌ Senha atual incorreta para {self.nome}!")
            return False
    
    def desativar_conta(self):
        """Desativa a conta do usuário"""
        self.ativo = False
        print(f"⚠️ Conta de {self.nome} foi desativada.")
    
    def ativar_conta(self):
        """Reativa a conta do usuário"""
        self.ativo = True
        print(f"✅ Conta de {self.nome} foi reativada.")
    
    def exibir_info(self):
        """Exibe informações do usuário (sem senha)"""
        status = "Ativo" if self.ativo else "Inativo"
        print(f"\n👤 Usuário: {self.nome}")
        print(f"📧 Email: {self.email}")
        print(f"📊 Status: {status}")

# Sistema de autenticação
class SistemaLogin:
    def __init__(self):
        self.usuarios = []
    
    def cadastrar_usuario(self, nome, email, senha):
        """Cadastra um novo usuário no sistema"""
        # Verifica se o email já existe
        for usuario in self.usuarios:
            if usuario.email == email:
                print(f"❌ Email {email} já está cadastrado!")
                return None
        
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        print(f"✅ Usuário {nome} cadastrado com sucesso!")
        return novo_usuario
    
    def login(self, email, senha):
        """Tenta fazer login com email e senha"""
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario.autenticar(email, senha)
        
        print(f"❌ Usuário com email {email} não encontrado!")
        return False
    
    def encontrar_usuario_por_email(self, email):
        """Encontra um usuário pelo email"""
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None
    
    def listar_usuarios(self):
        """Lista todos os usuários do sistema"""
        print(f"\n{'='*40}")
        print("📋 USUÁRIOS CADASTRADOS NO SISTEMA")
        print(f"{'='*40}")
        
        for i, usuario in enumerate(self.usuarios, 1):
            print(f"{i}. {usuario.nome} ({usuario.email}) - {'✅ Ativo' if usuario.ativo else '❌ Inativo'}")

# Demonstração do sistema
def demonstrar_sistema_usuarios():
    print("=== SISTEMA DE CADASTRO E AUTENTICAÇÃO DE USUÁRIOS ===\n")
    
    # Criando o sistema
    sistema = SistemaLogin()
    
    # Cadastrando usuários
    print("1. CADASTRANDO USUÁRIOS:")
    alice = sistema.cadastrar_usuario("Alice Silva", "alice@email.com", "senha123")
    bob = sistema.cadastrar_usuario("Bob Santos", "bob@email.com", "abc456")
    carol = sistema.cadastrar_usuario("Carol Oliveira", "carol@email.com", "minhasenha")
    
    # Listando usuários cadastrados
    sistema.listar_usuarios()
    
    # Testando autenticações
    print("\n2. TESTANDO AUTENTICAÇÕES:")
    
    print("\n--- Tentativas de Login Corretas ---")
    sistema.login("alice@email.com", "senha123")  # Alice correta
    sistema.login("bob@email.com", "abc456")      # Bob correta
    
    print("\n--- Tentativas de Login Incorretas ---")
    sistema.login("alice@email.com", "senha_errada")  # Alice senha errada
    sistema.login("bob@email.com", "123456")          # Bob senha errada
    sistema.login("email_inexistente@teste.com", "123")  # Email não cadastrado
    
    # Demonstrando que cada usuário tem seus próprios dados
    print("\n3. DEMONSTRANDO INSTÂNCIAS INDEPENDENTES:")
    
    # Cada usuário gerencia suas próprias credenciais
    print(f"\nAlice: nome='{alice.nome}', email='{alice.email}'")
    print(f"Bob: nome='{bob.nome}', email='{bob.email}'")
    print(f"Carol: nome='{carol.nome}', email='{carol.email}'")
    
    # Alteração de senha específica por usuário
    print("\n4. ALTERAÇÃO DE SENHAS:")
    alice.alterar_senha("senha123", "nova_senha_456")  # Alice altera sua senha
    alice.alterar_senha("senha_errada", "outra_senha") # Tentativa com senha atual errada
    
    # Testando login com nova senha
    print("\n5. TESTANDO NOVA SENHA:")
    sistema.login("alice@email.com", "nova_senha_456")  # Nova senha funciona
    sistema.login("alice@email.com", "senha123")        # Senha antiga não funciona mais
    
    # Demonstrando desativação de conta
    print("\n6. GERENCIAMENTO DE STATUS:")
    bob.desativar_conta()
    sistema.login("bob@email.com", "abc456")  # Tentativa de login com conta inativa
    bob.ativar_conta()
    sistema.login("bob@email.com", "abc456")  # Agora funciona novamente

# Executando a demonstração
if __name__ == "__main__":
    demonstrar_sistema_usuarios()