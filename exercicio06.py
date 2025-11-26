class Usuario:
    def __init__(self, nome, email, saldo_inicial=0):
        self.nome = nome
        self.email = email
        self._saldo = saldo_inicial
        self._pagamentos = []  # Histórico de pagamentos
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def pagamentos(self):
        return self._pagamentos.copy()
    
    def adicionar_saldo(self, valor, motivo=""):
        """Adiciona saldo ao usuário com registro"""
        if valor <= 0:
            print(f"❌ Valor deve ser positivo!")
            return False
        
        self._saldo += valor
        registro = f"+{valor} ({motivo})" if motivo else f"+{valor}"
        self._pagamentos.append(registro)
        print(f"💰 {self.nome} recebeu {valor} moedas. Saldo: {self._saldo}")
        return True
    
    def debitar_saldo(self, valor, motivo=""):
        """Debita saldo do usuário com validação"""
        if valor <= 0:
            print(f"❌ Valor deve ser positivo!")
            return False
        
        if self._saldo >= valor:
            self._saldo -= valor
            registro = f"-{valor} ({motivo})" if motivo else f"-{valor}"
            self._pagamentos.append(registro)
            print(f"💸 {self.nome} pagou {valor} moedas. Saldo: {self._saldo}")
            return True
        else:
            print(f"❌ Saldo insuficiente! Disponível: {self._saldo}, Necessário: {valor}")
            return False
    
    def exibir_extrato(self):
        """Exibe o extrato completo do usuário"""
        print(f"\n{'='*50}")
        print(f"📊 EXTRATO DE: {self.nome}")
        print(f"{'='*50}")
        print(f"📧 Email: {self.email}")
        print(f"💰 Saldo atual: {self._saldo} moedas")
        print(f"📋 Histórico de transações ({len(self._pagamentos)}):")
        
        for i, transacao in enumerate(self._pagamentos, 1):
            print(f"   {i}. {transacao}")
        
        print(f"{'='*50}")

class Pagamento:
    def __init__(self, usuario, valor, descricao=""):
        self.usuario = usuario
        self.valor = valor
        self.descricao = descricao
        self.status = "Pendente"  # Pendente, Processado, Falha
        self.data_criacao = "2024-01-01"  # Simulando data
    
    def processar(self):
        """Processa o pagamento e adiciona saldo ao usuário"""
        print(f"\n🔄 PROCESSANDO PAGAMENTO...")
        print(f"   Usuário: {self.usuario.nome}")
        print(f"   Valor: {self.valor} moedas")
        print(f"   Descrição: {self.descricao}")
        
        if self.valor <= 0:
            self.status = "Falha"
            print(f"❌ ERRO: Valor do pagamento deve ser positivo!")
            return False
        
        if self.status != "Pendente":
            print(f"⚠️  Pagamento já foi processado anteriormente!")
            return False
        
        # Processando o pagamento
        sucesso = self.usuario.adicionar_saldo(self.valor, f"Pagamento: {self.descricao}")
        
        if sucesso:
            self.status = "Processado"
            print(f"✅ PAGAMENTO PROCESSADO COM SUCESSO!")
            print(f"   Novo saldo de {self.usuario.nome}: {self.usuario.saldo} moedas")
            return True
        else:
            self.status = "Falha"
            print(f"❌ FALHA NO PROCESSAMENTO DO PAGAMENTO")
            return False
    
    def cancelar(self):
        """Cancela um pagamento pendente"""
        if self.status == "Pendente":
            self.status = "Cancelado"
            print(f"❌ Pagamento de {self.valor} para {self.usuario.nome} foi cancelado")
            return True
        else:
            print(f"⚠️  Não é possível cancelar um pagamento com status: {self.status}")
            return False
    
    def exibir_info(self):
        """Exibe informações do pagamento"""
        status_emoji = {
            "Pendente": "⏳",
            "Processado": "✅",
            "Falha": "❌",
            "Cancelado": "🚫"
        }
        
        emoji = status_emoji.get(self.status, "❓")
        print(f"\n{emoji} PAGAMENTO ID: {id(self)}")
        print(f"   Usuário: {self.usuario.nome}")
        print(f"   Valor: {self.valor} moedas")
        print(f"   Descrição: {self.descricao}")
        print(f"   Status: {self.status}")
        print(f"   Data: {self.data_criacao}")

# Sistema de Gestão de Pagamentos
class SistemaPagamentos:
    def __init__(self):
        self.pagamentos = []
    
    def criar_pagamento(self, usuario, valor, descricao=""):
        """Cria um novo pagamento"""
        pagamento = Pagamento(usuario, valor, descricao)
        self.pagamentos.append(pagamento)
        print(f"📄 Novo pagamento criado para {usuario.nome}")
        return pagamento
    
    def processar_todos_pendentes(self):
        """Processa todos os pagamentos pendentes"""
        print(f"\n🔄 PROCESSANDO TODOS OS PAGAMENTOS PENDENTES...")
        pendentes = [p for p in self.pagamentos if p.status == "Pendente"]
        
        if not pendentes:
            print("ℹ️  Nenhum pagamento pendente para processar")
            return
        
        for pagamento in pendentes:
            pagamento.processar()
    
    def listar_pagamentos(self):
        """Lista todos os pagamentos do sistema"""
        print(f"\n{'='*60}")
        print(f"📋 RELATÓRIO DE PAGAMENTOS ({len(self.pagamentos)} no total)")
        print(f"{'='*60}")
        
        status_count = {"Pendente": 0, "Processado": 0, "Falha": 0, "Cancelado": 0}
        
        for pagamento in self.pagamentos:
            status_count[pagamento.status] += 1
            pagamento.exibir_info()
        
        print(f"\n📊 RESUMO:")
        for status, count in status_count.items():
            if count > 0:
                print(f"   {status}: {count}")

# Demonstração do sistema
def demonstrar_sistema_pagamentos():
    print("=== SISTEMA DE PAGAMENTOS ===\n")
    
    # Criando usuários
    print("1. CRIANDO USUÁRIOS:")
    usuario1 = Usuario("Alice Silva", "alice@email.com", 100)
    usuario2 = Usuario("Bob Santos", "bob@empresa.com", 50)
    usuario3 = Usuario("Carol Oliveira", "carol@loja.com", 200)
    
    # Exibindo saldos iniciais
    usuario1.exibir_extrato()
    usuario2.exibir_extrato()
    
    # Criando sistema de pagamentos
    sistema = SistemaPagamentos()
    
    # Criando pagamentos
    print("\n2. CRIANDO PAGAMENTOS:")
    pagamento1 = sistema.criar_pagamento(usuario1, 150, "Recarga mensal")
    pagamento2 = sistema.criar_pagamento(usuario2, 75, "Bônus promocional")
    pagamento3 = sistema.criar_pagamento(usuario3, 200, "Presente de aniversário")
    pagamento4 = sistema.criar_pagamento(usuario1, -50, "Pagamento inválido")  # Valor negativo
    
    # Processando pagamentos individuais
    print("\n3. PROCESSAMENTO INDIVIDUAL:")
    pagamento1.processar()  # Processa com sucesso
    pagamento4.processar()  # Deve falhar (valor negativo)
    
    # Criando mais pagamentos
    print("\n4. MAIS PAGAMENTOS:")
    pagamento5 = sistema.criar_pagamento(usuario2, 100, "Cashback")
    pagamento6 = sistema.criar_pagamento(usuario3, 50, "Recompensa diária")
    
    # Processando todos os pendentes
    print("\n5. PROCESSAMENTO EM LOTE:")
    sistema.processar_todos_pendentes()
    
    # Tentativa de processar novamente
    print("\n6. TENTATIVA DE REPROCESSAMENTO:")
    pagamento1.processar()  # Já foi processado
    
    # Operações de cancelamento
    print("\n7. OPERAÇÕES DE CANCELAMENTO:")
    pagamento7 = sistema.criar_pagamento(usuario1, 300, "Pagamento teste")
    pagamento7.cancelar()  # Cancela pagamento pendente
    pagamento7.processar()  # Tenta processar cancelado (deve falhar)
    
    # Extratos finais
    print("\n8. EXTRATOS FINAIS:")
    usuario1.exibir_extrato()
    usuario2.exibir_extrato()
    usuario3.exibir_extrato()
    
    # Relatório do sistema
    print("\n9. RELATÓRIO DO SISTEMA:")
    sistema.listar_pagamentos()

# Demonstração da interação entre classes
def demonstrar_interacao_classes():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO DA INTERAÇÃO ENTRE CLASSES")
    print("="*60)
    
    # Criando objetos
    usuario = Usuario("João Teste", "joao@teste.com", 100)
    pagamento = Pagamento(usuario, 500, "Depósito inicial")
    
    print("\n🔗 OBJETOS CRIADOS:")
    print(f"Usuario: {usuario.nome} (Saldo: {usuario.saldo})")
    print(f"Pagamento: {pagamento.valor} para {pagamento.usuario.nome}")
    
    print("\n🔄 INTERAÇÃO ENTRE OBJETOS:")
    print("Antes do processamento:")
    print(f"  - Saldo do usuário: {usuario.saldo}")
    print(f"  - Status do pagamento: {pagamento.status}")
    
    # A interação acontece aqui!
    pagamento.processar()
    
    print("\nApós o processamento:")
    print(f"  - Saldo do usuário: {usuario.saldo}")
    print(f"  - Status do pagamento: {pagamento.status}")
    
    print(f"\n💡 O pagamento INTERAGIU com o usuário:")
    print(f"   pagamento.processar() → usuario.adicionar_saldo()")
    print(f"   Objeto Pagamento → Objeto Usuario")

# Executando as demonstrações
if __name__ == "__main__":
    demonstrar_sistema_pagamentos()
    demonstrar_interacao_classes()