class Jogador:
    def __init__(self, nome, saldo_inicial=100):
        self.nome = nome
        self._saldo = saldo_inicial  # _ indica "protegido"
        self._itens = []  # Lista de itens do inventário
        self.nivel = 1
        self.experiencia = 0
    
    @property
    def saldo(self):
        """Permite ler o saldo, mas não modificar diretamente"""
        return self._saldo
    
    @property
    def itens(self):
        """Retorna uma cópia da lista de itens para proteger o original"""
        return self._itens.copy()
    
    def adicionar_saldo(self, quantidade):
        """Adiciona saldo ao jogador com validações"""
        if quantidade <= 0:
            print(f"❌ {self.nome}: Quantidade deve ser positiva!")
            return False
        
        self._saldo += quantidade
        print(f"💰 {self.nome} recebeu {quantidade} moedas. Saldo atual: {self._saldo}")
        return True
    
    def comprar_item(self, item, preco):
        """Compra um item se o jogador tiver saldo suficiente"""
        if preco <= 0:
            print(f"❌ {self.nome}: Preço do item deve ser positivo!")
            return False
        
        if self._saldo >= preco:
            self._saldo -= preco
            self._itens.append(item)
            print(f"🛍️ {self.nome} comprou '{item}' por {preco} moedas!")
            print(f"   Saldo restante: {self._saldo} moedas")
            print(f"   Itens no inventário: {len(self._itens)}")
            return True
        else:
            print(f"❌ {self.nome} não tem saldo suficiente para comprar '{item}'!")
            print(f"   Saldo necessário: {preco} | Saldo atual: {self._saldo}")
            return False
    
    def vender_item(self, item, preco_venda):
        """Vende um item do inventário"""
        if item in self._itens:
            self._itens.remove(item)
            self._saldo += preco_venda
            print(f"💸 {self.nome} vendeu '{item}' por {preco_venda} moedas!")
            print(f"   Novo saldo: {self._saldo} moedas")
            return True
        else:
            print(f"❌ {self.nome} não possui o item '{item}' para vender!")
            return False
    
    def usar_item(self, item):
        """Usa um item do inventário (remove após uso)"""
        if item in self._itens:
            self._itens.remove(item)
            print(f"🎯 {self.nome} usou o item '{item}'")
            return True
        else:
            print(f"❌ {self.nome} não possui o item '{item}'!")
            return False
    
    def adicionar_experiencia(self, xp):
        """Adiciona experiência e sobe de nível se necessário"""
        if xp <= 0:
            print(f"❌ Experiência deve ser positiva!")
            return
        
        self.experiencia += xp
        nivel_anterior = self.nivel
        
        # Sistema simples de level up (100 XP por nível)
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.nivel += 1
            print(f"🎉 {self.nome} subiu para o nível {self.nivel}!")
        
        if self.nivel > nivel_anterior:
            # Recompensa por subir de nível
            recompensa = self.nivel * 50
            self.adicionar_saldo(recompensa)
    
    def exibir_status(self):
        """Exibe o status completo do jogador"""
        print(f"\n{'='*50}")
        print(f"🎮 STATUS DO JOGADOR: {self.nome}")
        print(f"{'='*50}")
        print(f"📊 Nível: {self.nivel}")
        print(f"⭐ Experiência: {self.experiencia}/{(self.nivel + 1) * 100}")
        print(f"💰 Saldo: {self._saldo} moedas")
        print(f"🎒 Itens no inventário ({len(self._itens)}):")
        
        if self._itens:
            for i, item in enumerate(self._itens, 1):
                print(f"   {i}. {item}")
        else:
            print("   (Inventário vazio)")
        print(f"{'='*50}")

# Sistema de Loja do Jogo
class LojaJogo:
    def __init__(self):
        self.itens_disponiveis = {
            "Poção de Vida": 50,
            "Poção de Mana": 75,
            "Espada de Ferro": 200,
            "Escudo de Madeira": 150,
            "Arco Longo": 300,
            "Armadura de Couro": 250,
            "Pergaminho de Fogo": 100,
            "Chave Mística": 25
        }
    
    def listar_itens(self):
        """Lista todos os itens disponíveis na loja"""
        print(f"\n🏪 LOJA - ITENS DISPONÍVEIS:")
        print("-" * 35)
        for item, preco in self.itens_disponiveis.items():
            print(f"🛒 {item}: {preco} moedas")
    
    def comprar_da_loja(self, jogador, nome_item):
        """Um jogador compra um item da loja"""
        if nome_item in self.itens_disponiveis:
            preco = self.itens_disponiveis[nome_item]
            return jogador.comprar_item(nome_item, preco)
        else:
            print(f"❌ Item '{nome_item}' não está disponível na loja!")
            return False

# Demonstração do sistema
def demonstrar_sistema_jogadores():
    print("=== SISTEMA DE GESTÃO DE JOGADORES ===\n")
    
    # Criando jogadores
    print("1. CRIANDO JOGADORES:")
    jogador1 = Jogador("Aragorn", 200)
    jogador2 = Jogador("Gandalf", 150)
    jogador3 = Jogador("Legolas", 300)
    
    # Exibindo status iniciais
    jogador1.exibir_status()
    jogador2.exibir_status()
    jogador3.exibir_status()
    
    # Criando a loja
    loja = LojaJogo()
    
    # Operações de compra
    print("\n2. OPERAÇÕES DE COMPRA:")
    
    print("\n--- Compras bem-sucedidas ---")
    jogador1.comprar_item("Espada Lendária", 180)  # Compra direta
    loja.comprar_da_loja(jogador2, "Poção de Vida")  # Compra na loja
    loja.comprar_da_loja(jogador3, "Arco Longo")
    
    print("\n--- Tentativas de compra com saldo insuficiente ---")
    jogador1.comprar_item("Armadura Divina", 500)  # Muito cara!
    loja.comprar_da_loja(jogador2, "Armadura de Couro")  # Sem saldo suficiente
    
    print("\n--- Mais compras ---")
    loja.comprar_da_loja(jogador1, "Escudo de Madeira")
    loja.comprar_da_loja(jogador3, "Poção de Mana")
    loja.comprar_da_loja(jogador3, "Pergaminho de Fogo")
    
    # Adicionando saldo
    print("\n3. ADICIONANDO SALDO:")
    jogador1.adicionar_saldo(100)
    jogador2.adicionar_saldo(200)
    
    # Tentativa de adicionar saldo inválido
    jogador3.adicionar_saldo(-50)  # Valor negativo
    
    # Mais compras após adicionar saldo
    print("\n4. MAIS COMPRAS APÓS GANHAR SALDO:")
    loja.comprar_da_loja(jogador2, "Armadura de Couro")  # Agora funciona!
    
    # Operações com itens
    print("\n5. OPERAÇÕES COM ITENS:")
    jogador3.usar_item("Poção de Mana")
    jogador1.vender_item("Escudo de Madeira", 75)  # Vende por metade do preço
    
    # Tentativa de usar item que não tem
    jogador2.usar_item("Espada Lendária")  # Não possui
    
    # Sistema de experiência
    print("\n6. SISTEMA DE EXPERIÊNCIA:")
    jogador1.adicionar_experiencia(80)
    jogador1.adicionar_experiencia(50)  # Deve subir de nível
    jogador2.adicionar_experiencia(120)  # Deve subir de nível
    jogador3.adicionar_experiencia(200)  # Deve subir 2 níveis
    
    # Status finais
    print("\n7. STATUS FINAIS:")
    jogador1.exibir_status()
    jogador2.exibir_status()
    jogador3.exibir_status()
    
    # Listar itens da loja
    print("\n8. CATÁLOGO DA LOJA:")
    loja.listar_itens()

# Demonstração do encapsulamento
def demonstrar_encapsulamento():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO DO ENCAPSULAMENTO")
    print("="*60)
    
    jogador = Jogador("TestPlayer", 100)
    
    print("\n✅ Acesso CONTROLADO aos dados:")
    print(f"Nome: {jogador.nome}")  # Acesso direto permitido
    print(f"Saldo: {jogador.saldo}")  # Via property (apenas leitura)
    print(f"Itens: {jogador.itens}")  # Cópia protegida
    
    print("\n❌ Tentativas de modificação DIRETA (não permitidas):")
    print("jogador._saldo = 1000  # Tecnicamente possível, mas contra as regras")
    print("jogador._itens.append('Item Ilegal')  # Violação do encapsulamento")
    
    print("\n✅ Modificação apenas através dos MÉTODOS:")
    jogador.adicionar_saldo(50)  # Método controlado
    jogador.comprar_item("Poção", 30)  # Com validações
    
    print(f"\nSaldo após operações: {jogador.saldo}")
    print(f"Itens após operações: {jogador.itens}")

# Executando as demonstrações
if __name__ == "__main__":
    demonstrar_sistema_jogadores()
    demonstrar_encapsulamento()