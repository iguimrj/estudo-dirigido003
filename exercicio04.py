class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    
    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"

class Pedido:
    def __init__(self, numero_pedido, cliente=""):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.produtos = []  # Lista de produtos no pedido
        self.status = "Aberto"
    
    def adicionar_produto(self, produto):
        """Adiciona um produto ao pedido"""
        self.produtos.append(produto)
        print(f"✅ '{produto.nome}' adicionado ao pedido {self.numero_pedido}")
    
    def remover_produto(self, nome_produto):
        """Remove um produto do pedido pelo nome"""
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                self.produtos.remove(produto)
                print(f"❌ '{produto.nome}' removido do pedido {self.numero_pedido}")
                return True
        print(f"⚠️ Produto '{nome_produto}' não encontrado no pedido")
        return False
    
    def listar_produtos(self):
        """Lista todos os produtos do pedido"""
        if not self.produtos:
            print(f"📭 Pedido {self.numero_pedido} está vazio")
            return
        
        print(f"\n🛒 PRODUTOS NO PEDIDO {self.numero_pedido}:")
        print("-" * 40)
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto}")
    
    def calcular_valor_total(self):
        """Calcula o valor total do pedido"""
        total = sum(produto.preco for produto in self.produtos)
        print(f"💰 TOTAL DO PEDIDO {self.numero_pedido}: R$ {total:.2f}")
        return total
    
    def finalizar_pedido(self):
        """Finaliza o pedido"""
        if not self.produtos:
            print("❌ Não é possível finalizar um pedido vazio!")
            return False
        
        self.status = "Finalizado"
        total = self.calcular_valor_total()
        print(f"🎉 Pedido {self.numero_pedido} finalizado com sucesso!")
        return True
    
    def exibir_resumo(self):
        """Exibe um resumo completo do pedido"""
        print(f"\n{'='*50}")
        print(f"📋 RESUMO DO PEDIDO {self.numero_pedido}")
        print(f"{'='*50}")
        print(f"👤 Cliente: {self.cliente if self.cliente else 'Não informado'}")
        print(f"📊 Status: {self.status}")
        print(f"📦 Quantidade de itens: {len(self.produtos)}")
        
        self.listar_produtos()
        self.calcular_valor_total()

# Sistema de E-commerce
class LojaVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        self.pedidos = []
        self.contador_pedidos = 1
    
    def adicionar_produto_catalogo(self, nome, preco):
        """Adiciona um produto ao catálogo da loja"""
        produto = Produto(nome, preco)
        self.catalogo.append(produto)
        print(f"📦 '{nome}' adicionado ao catálogo por R$ {preco:.2f}")
        return produto
    
    def listar_catalogo(self):
        """Lista todos os produtos do catálogo"""
        print(f"\n🏪 CATÁLOGO DA LOJA {self.nome}:")
        print("-" * 40)
        for i, produto in enumerate(self.catalogo, 1):
            print(f"{i}. {produto}")
    
    def criar_pedido(self, cliente=""):
        """Cria um novo pedido"""
        pedido = Pedido(self.contador_pedidos, cliente)
        self.pedidos.append(pedido)
        self.contador_pedidos += 1
        print(f"🆕 Pedido {pedido.numero_pedido} criado para {cliente if cliente else 'cliente não identificado'}")
        return pedido
    
    def encontrar_produto_por_nome(self, nome):
        """Encontra um produto no catálogo pelo nome"""
        for produto in self.catalogo:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

# Demonstração do sistema
def demonstrar_sistema_pedidos():
    print("=== SISTEMA DE E-COMMERCE - PEDIDOS ===\n")
    
    # Criando a loja
    loja = LojaVirtual("TechStore")
    
    # Populando o catálogo
    print("1. POPULANDO CATÁLOGO:")
    loja.adicionar_produto_catalogo("Notebook Gamer", 4500.00)
    loja.adicionar_produto_catalogo("Mouse Sem Fio", 89.90)
    loja.adicionar_produto_catalogo("Teclado Mecânico", 350.00)
    loja.adicionar_produto_catalogo("Monitor 24\"", 899.00)
    loja.adicionar_produto_catalogo("Headphone Bluetooth", 299.90)
    
    # Listando catálogo
    loja.listar_catalogo()
    
    # Criando pedidos
    print("\n2. CRIANDO PEDIDOS:")
    pedido1 = loja.criar_pedido("Alice Silva")
    pedido2 = loja.criar_pedido("Bob Santos")
    
    # Adicionando produtos aos pedidos
    print("\n3. ADICIONANDO PRODUTOS AOS PEDIDOS:")
    
    print("\n--- Pedido 1 (Alice) ---")
    pedido1.adicionar_produto(loja.encontrar_produto_por_nome("Notebook Gamer"))
    pedido1.adicionar_produto(loja.encontrar_produto_por_nome("Mouse Sem Fio"))
    pedido1.adicionar_produto(loja.encontrar_produto_por_nome("Headphone Bluetooth"))
    
    print("\n--- Pedido 2 (Bob) ---")
    pedido2.adicionar_produto(loja.encontrar_produto_por_nome("Monitor 24\""))
    pedido2.adicionar_produto(loja.encontrar_produto_por_nome("Teclado Mecânico"))
    
    # Listando pedidos
    print("\n4. LISTANDO PEDIDOS:")
    pedido1.listar_produtos()
    pedido2.listar_produtos()
    
    # Operações nos pedidos
    print("\n5. OPERAÇÕES NOS PEDIDOS:")
    
    # Removendo um produto
    pedido1.remover_produto("Mouse Sem Fio")
    
    # Adicionando mais produtos
    pedido2.adicionar_produto(loja.encontrar_produto_por_nome("Mouse Sem Fio"))
    
    # Cálculos de valor
    print("\n6. CÁLCULOS DE VALOR:")
    pedido1.calcular_valor_total()
    pedido2.calcular_valor_total()
    
    # Resumos finais
    print("\n7. RESUMOS FINAIS:")
    pedido1.exibir_resumo()
    pedido2.exibir_resumo()
    
    # Finalizando pedidos
    print("\n8. FINALIZANDO PEDIDOS:")
    pedido1.finalizar_pedido()
    pedido2.finalizar_pedido()

# Versão simplificada conforme solicitado
def demonstracao_simplificada():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO SIMPLIFICADA - COMPOSIÇÃO DE CLASSES")
    print("="*60)
    
    # Criando produtos
    produto1 = Produto("Camiseta", 29.90)
    produto2 = Produto("Calça Jeans", 89.90)
    produto3 = Produto("Tênis", 199.90)
    
    # Criando pedido
    pedido = Pedido(1, "João Silva")
    
    # Adicionando produtos ao pedido
    pedido.adicionar_produto(produto1)
    pedido.adicionar_produto(produto2)
    pedido.adicionar_produto(produto3)
    
    # Listando produtos
    pedido.listar_produtos()
    
    # Calculando total
    pedido.calcular_valor_total()
    
    # Demonstrando a composição
    print(f"\n💡 O pedido contém {len(pedido.produtos)} objetos Produto:")
    for i, produto in enumerate(pedido.produtos, 1):
        print(f"   {i}. {produto} (objeto Produto)")

# Executando as demonstrações
if __name__ == "__main__":
    demonstrar_sistema_pedidos()
    demonstracao_simplificada()