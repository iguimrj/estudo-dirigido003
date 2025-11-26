class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def adicionar_estoque(self, qtd):
        """Adiciona quantidade ao estoque deste produto"""
        self.quantidade += qtd
        print(f"Adicionadas {qtd} unidades ao produto '{self.nome}'. Novo total: {self.quantidade}")
    
    def remover_estoque(self, qtd):
        """Remove quantidade do estoque deste produto"""
        if self.quantidade >= qtd:
            self.quantidade -= qtd
            print(f"Removidas {qtd} unidades do produto '{self.nome}'. Novo total: {self.quantidade}")
            return True
        else:
            print(f"Estoque insuficiente para '{self.nome}'! Tem apenas {self.quantidade} unidades.")
            return False
    
    def valor_total(self):
        """Calcula o valor total em estoque para este produto"""
        total = self.quantidade * self.preco
        print(f"Valor total em estoque para '{self.nome}': R$ {total:.2f}")
        return total
    
    def __str__(self):
        """Representação em string do produto"""
        return f"Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f} | Valor Total: R$ {self.valor_total():.2f}"

class SistemaEstoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, nome, quantidade, preco):
        """Adiciona um novo produto ao sistema"""
        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)
        print(f"Produto '{nome}' adicionado ao sistema.")
        return produto
    
    def encontrar_produto(self, nome):
        """Encontra um produto pelo nome"""
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None
    
    def adicionar_estoque(self, produto_nome, qtd):
        """Adiciona estoque a um produto"""
        produto = self.encontrar_produto(produto_nome)
        if produto:
            produto.adicionar_estoque(qtd)
        else:
            print(f"Produto '{produto_nome}' não encontrado!")
    
    def remover_estoque(self, produto_nome, qtd):
        """Remove estoque de um produto"""
        produto = self.encontrar_produto(produto_nome)
        if produto:
            return produto.remover_estoque(qtd)
        else:
            print(f"Produto '{produto_nome}' não encontrado!")
            return False
    
    def valor_total_produto(self, produto_nome):
        """Calcula valor total de um produto específico"""
        produto = self.encontrar_produto(produto_nome)
        if produto:
            return produto.valor_total()
        else:
            print(f"Produto '{produto_nome}' não encontrado!")
            return 0
    
    def valor_total_estoque(self):
        """Calcula o valor total de todo o estoque"""
        total = sum(produto.quantidade * produto.preco for produto in self.produtos)
        print(f"Valor total do estoque: R$ {total:.2f}")
        return total
    
    def listar_estoque(self):
        """Lista todos os produtos em estoque"""
        print("\n--- SISTEMA DE ESTOQUE ---")
        for produto in self.produtos:
            print(produto)
        self.valor_total_estoque()

# Exemplo de uso
if __name__ == "__main__":
    # Criando o sistema
    sistema = SistemaEstoque()
    
    # Adicionando produtos
    notebook = sistema.adicionar_produto("Notebook", 10, 2500.00)
    mouse = sistema.adicionar_produto("Mouse", 50, 45.90)
    teclado = sistema.adicionar_produto("Teclado", 30, 120.00)
    
    print("\n--- OPERAÇÕES NO ESTOQUE ---")
    # Operações no estoque - diferentes formas de fazer
    sistema.adicionar_estoque("Notebook", 5)           # Via sistema
    mouse.adicionar_estoque(20)                        # Direto no objeto
    sistema.remover_estoque("Mouse", 15)
    teclado.remover_estoque(5)                         # Direto no objeto
    
    print("\n--- CÁLCULOS DE VALOR ---")
    # Calculando valores totais
    sistema.valor_total_produto("Notebook")
    notebook.valor_total()                             # Direto no objeto
    sistema.valor_total_produto("Teclado")
    
    print("\n--- RELATÓRIO FINAL ---")
    # Listando estoque completo
    sistema.listar_estoque()
    
    # Tentativa com produto inexistente
    sistema.remover_estoque("Monitor", 5)