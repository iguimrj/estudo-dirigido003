def criar_sistema_estoque():
    """Cria um sistema de estoque isolado"""
    estoque = {}
    
    def adicionar_produto(nome, quantidade, preco):
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
    
    def adicionar_estoque(produto, qtd):
        if produto in estoque:
            estoque[produto]['quantidade'] += qtd
        else:
            print(f"Produto {produto} não encontrado!")
    
    def remover_estoque(produto, qtd):
        if produto in estoque:
            if estoque[produto]['quantidade'] >= qtd:
                estoque[produto]['quantidade'] -= qtd
            else:
                print("Estoque insuficiente!")
        else:
            print(f"Produto {produto} não encontrado!")
    
    def valor_total(produto):
        if produto in estoque:
            return estoque[produto]['quantidade'] * estoque[produto]['preco']
        return 0
    
    return {
        'adicionar_produto': adicionar_produto,
        'adicionar_estoque': adicionar_estoque,
        'remover_estoque': remover_estoque,
        'valor_total': valor_total,
        'get_estoque': lambda: estoque
    }

# Uso
sistema = criar_sistema_estoque()
sistema['adicionar_produto']('Notebook', 10, 2500.00)
sistema['adicionar_estoque']('Notebook', 5)
print(f"Valor total: R$ {sistema['valor_total']('Notebook'):.2f}")