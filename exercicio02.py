class SistemaEstoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, nome, quantidade, preco):
        """Adiciona um novo produto ao sistema"""
        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)
        print(f"✅ Produto '{nome}' adicionado ao sistema.")
        return produto
    
    def encontrar_produto(self, nome):
        """Encontra um produto pelo nome"""
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None
    
    def listar_todos_produtos(self):
        """Lista todos os produtos do sistema"""
        if not self.produtos:
            print("Nenhum produto cadastrado no sistema.")
            return
        
        print(f"\n{'='*50}")
        print("📦 RELATÓRIO COMPLETO DO ESTOQUE")
        print(f"{'='*50}")
        
        for produto in self.produtos:
            produto.exibir_info()
        
        # Total geral
        total_geral = sum(produto.valor_total() for produto in self.produtos)
        print(f"\n💰 VALOR TOTAL DO ESTOQUE: R$ {total_geral:.2f}")

# Exemplo completo de uso
def demonstrar_sistema():
    sistema = SistemaEstoque()
    
    # Cadastrando produtos
    sistema.adicionar_produto("Notebook Gamer", 3, 4500.00)
    sistema.adicionar_produto("Mouse Sem Fio", 50, 45.90)
    sistema.adicionar_produto("Monitor 24\"", 8, 899.00)
    sistema.adicionar_produto("Headphone Bluetooth", 12, 199.90)
    
    # Operações específicas em produtos
    print("\n🎯 OPERAÇÕES ESPECÍFICAS:")
    
    # Encontrando e manipulando produtos específicos
    notebook = sistema.encontrar_produto("notebook gamer")
    if notebook:
        notebook.adicionar(2)
        notebook.remover(1)
    
    mouse = sistema.encontrar_produto("mouse sem fio")
    if mouse:
        mouse.adicionar(25)
        mouse.remover(40)  # Deve falhar
        mouse.remover(30)  # Deve funcionar
    
    # Relatório final
    sistema.listar_todos_produtos()

# Executando a demonstração
if __name__ == "__main__":
    demonstrar_sistema()