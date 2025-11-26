class Livro:
    def __init__(self, titulo, autor, ano_publicacao, isbn=""):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn
        self.disponivel = True
        self.quantidade_emprestimos = 0
        self.ultimo_emprestimo = None
    
    def emprestar(self):
        """Marca o livro como emprestado se estiver disponível"""
        if self.disponivel:
            self.disponivel = False
            self.quantidade_emprestimos += 1
            self.ultimo_emprestimo = "2024-01-01"  # Data simulada
            print(f"📖 '{self.titulo}' foi emprestado com sucesso!")
            return True
        else:
            print(f"❌ '{self.titulo}' já está emprestado!")
            return False
    
    def devolver(self):
        """Marca o livro como disponível"""
        if not self.disponivel:
            self.disponivel = True
            print(f"✅ '{self.titulo}' foi devolvido e está disponível novamente!")
            return True
        else:
            print(f"⚠️  '{self.titulo}' já está disponível!")
            return False
    
    def exibir_info(self):
        """Exibe informações completas do livro"""
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        emprestimos = f"({self.quantidade_emprestimos} empréstimos)"
        
        print(f"\n📚 {self.titulo}")
        print(f"   👤 Autor: {self.autor}")
        print(f"   📅 Ano: {self.ano_publicacao}")
        print(f"   🏷️  ISBN: {self.isbn if self.isbn else 'Não informado'}")
        print(f"   📊 Status: {status} {emprestimos if self.quantidade_emprestimos > 0 else ''}")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.emprestimos_ativos = 0
    
    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca"""
        # Verificar se o livro já existe (por título e autor)
        for livro_existente in self.livros:
            if (livro_existente.titulo.lower() == livro.titulo.lower() and 
                livro_existente.autor.lower() == livro.autor.lower()):
                print(f"⚠️  O livro '{livro.titulo}' já existe na biblioteca!")
                return False
        
        self.livros.append(livro)
        print(f"✅ '{livro.titulo}' foi adicionado à biblioteca!")
        return True
    
    def adicionar_livro_detalhes(self, titulo, autor, ano_publicacao, isbn=""):
        """Adiciona um livro usando detalhes individuais"""
        livro = Livro(titulo, autor, ano_publicacao, isbn)
        return self.adicionar_livro(livro)
    
    def encontrar_livro(self, titulo):
        """Encontra um livro pelo título (busca parcial)"""
        livros_encontrados = []
        titulo_lower = titulo.lower()
        
        for livro in self.livros:
            if titulo_lower in livro.titulo.lower():
                livros_encontrados.append(livro)
        
        return livros_encontrados
    
    def encontrar_livro_exato(self, titulo):
        """Encontra um livro exato pelo título"""
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
    
    def emprestar_livro(self, titulo):
        """Empresta um livro se estiver disponível"""
        livro = self.encontrar_livro_exato(titulo)
        
        if not livro:
            print(f"❌ Livro '{titulo}' não encontrado na biblioteca!")
            return False
        
        if livro.emprestar():
            self.emprestimos_ativos += 1
            return True
        return False
    
    def devolver_livro(self, titulo):
        """Devolve um livro emprestado"""
        livro = self.encontrar_livro_exato(titulo)
        
        if not livro:
            print(f"❌ Livro '{titulo}' não encontrado na biblioteca!")
            return False
        
        if livro.devolver():
            self.emprestimos_ativos -= 1
            return True
        return False
    
    def listar_disponiveis(self):
        """Lista todos os livros disponíveis para empréstimo"""
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        
        if not disponiveis:
            print("📭 Nenhum livro disponível no momento!")
            return
        
        print(f"\n📚 LIVROS DISPONÍVEIS ({len(disponiveis)}):")
        print("-" * 50)
        for i, livro in enumerate(disponiveis, 1):
            print(f"{i}. '{livro.titulo}' - {livro.autor}")
    
    def listar_emprestados(self):
        """Lista todos os livros atualmente emprestados"""
        emprestados = [livro for livro in self.livros if not livro.disponivel]
        
        if not emprestados:
            print("✅ Todos os livros estão na biblioteca!")
            return
        
        print(f"\n📖 LIVROS EMPRESTADOS ({len(emprestados)}):")
        print("-" * 50)
        for i, livro in enumerate(emprestados, 1):
            print(f"{i}. '{livro.titulo}' - {livro.autor}")
    
    def listar_todos_livros(self):
        """Lista todos os livros da biblioteca"""
        if not self.livros:
            print("📚 A biblioteca está vazia!")
            return
        
        print(f"\n{'='*60}")
        print(f"📚 BIBLIOTECA {self.nome.upper()} - CATÁLOGO COMPLETO")
        print(f"{'='*60}")
        print(f"📊 Total de livros: {len(self.livros)}")
        print(f"📖 Empréstimos ativos: {self.emprestimos_ativos}")
        print(f"✅ Disponíveis: {len([l for l in self.livros if l.disponivel])}")
        
        for i, livro in enumerate(self.livros, 1):
            status = "✅" if livro.disponivel else "❌"
            print(f"\n{i}. {status} '{livro.titulo}'")
            print(f"   👤 {livro.autor} | 📅 {livro.ano_publicacao}")
    
    def buscar_por_autor(self, autor):
        """Busca livros por autor"""
        livros_autor = [livro for livro in self.livros if autor.lower() in livro.autor.lower()]
        
        if not livros_autor:
            print(f"❌ Nenhum livro encontrado do autor '{autor}'")
            return
        
        print(f"\n👤 LIVROS DO AUTOR '{autor}' ({len(livros_autor)}):")
        print("-" * 50)
        for i, livro in enumerate(livros_autor, 1):
            status = "✅ Disponível" if livro.disponivel else "❌ Emprestado"
            print(f"{i}. '{livro.titulo}' - {status}")

# Demonstração do sistema
def demonstrar_sistema_biblioteca():
    print("=== SISTEMA DE BIBLIOTECA ===\n")
    
    # Criando a biblioteca
    biblioteca = Biblioteca("Central da Cidade")
    
    # Adicionando livros
    print("1. ADICIONANDO LIVROS À BIBLIOTECA:")
    biblioteca.adicionar_livro_detalhes("Dom Casmurro", "Machado de Assis", 1899, "978-85-7232-144-9")
    biblioteca.adicionar_livro_detalhes("O Cortiço", "Aluísio Azevedo", 1890, "978-85-7232-145-6")
    biblioteca.adicionar_livro_detalhes("1984", "George Orwell", 1949, "978-85-359-0276-4")
    biblioteca.adicionar_livro_detalhes("A Revolução dos Bichos", "George Orwell", 1945, "978-85-359-0277-1")
    biblioteca.adicionar_livro_detalhes("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "978-85-01-05135-9")
    
    # Tentativa de adicionar livro duplicado
    biblioteca.adicionar_livro_detalhes("Dom Casmurro", "Machado de Assis", 1899)
    
    # Listando livros
    print("\n2. CATÁLOGO INICIAL:")
    biblioteca.listar_todos_livros()
    
    # Operações de empréstimo
    print("\n3. OPERAÇÕES DE EMPRÉSTIMO:")
    
    print("\n--- Empréstimos bem-sucedidos ---")
    biblioteca.emprestar_livro("Dom Casmurro")
    biblioteca.emprestar_livro("1984")
    
    print("\n--- Tentativa de empréstimo duplicado ---")
    biblioteca.emprestar_livro("Dom Casmurro")  # Já emprestado!
    
    print("\n--- Mais empréstimos ---")
    biblioteca.emprestar_livro("A Revolução dos Bichos")
    
    # Listando disponíveis e emprestados
    print("\n4. SITUAÇÃO ATUAL:")
    biblioteca.listar_disponiveis()
    biblioteca.listar_emprestados()
    
    # Operações de devolução
    print("\n5. OPERAÇÕES DE DEVOLUÇÃO:")
    biblioteca.devolver_livro("Dom Casmurro")
    biblioteca.devolver_livro("1984")
    
    # Tentativa de devolução de livro disponível
    biblioteca.devolver_livro("O Cortiço")  # Já está disponível
    
    # Buscas
    print("\n6. SISTEMA DE BUSCA:")
    biblioteca.buscar_por_autor("Orwell")
    biblioteca.buscar_por_autor("Machado")
    
    # Situação final
    print("\n7. SITUAÇÃO FINAL:")
    biblioteca.listar_todos_livros()

# Demonstração das regras de negócio
def demonstrar_regras_negocio():
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO DAS REGRAS DE NEGÓCIO")
    print("="*60)
    
    # Criando biblioteca de teste
    bib = Biblioteca("Teste")
    bib.adicionar_livro_detalhes("Livro Teste", "Autor Teste", 2024)
    
    livro = bib.encontrar_livro_exato("Livro Teste")
    
    print("\n📖 REGRAS DE NEGÓCIO IMPLEMENTADAS:")
    
    print("\n1. ✅ EMPRÉSTIMO VÁLIDO:")
    print("   Livro disponível → Pode ser emprestado")
    livro.exibir_info()
    bib.emprestar_livro("Livro Teste")
    
    print("\n2. ❌ EMPRÉSTIMO INVÁLIDO (duplicado):")
    print("   Livro já emprestado → Não pode ser emprestado novamente")
    bib.emprestar_livro("Livro Teste")  # Deve falhar
    
    print("\n3. ✅ DEVOLUÇÃO VÁLIDA:")
    print("   Livro emprestado → Pode ser devolvido")
    bib.devolver_livro("Livro Teste")
    
    print("\n4. ⚠️  DEVOLUÇÃO INVÁLIDA:")
    print("   Livro já disponível → Devolução desnecessária")
    bib.devolver_livro("Livro Teste")  # Já está disponível
    
    print("\n5. 🔄 CICLO COMPLETO:")
    print("   Disponível → Emprestado → Disponível")
    bib.emprestar_livro("Livro Teste")
    bib.devolver_livro("Livro Teste")
    
    print(f"\n📊 Estatísticas do livro:")
    print(f"   Quantidade de empréstimos: {livro.quantidade_emprestimos}")

# Executando as demonstrações
if __name__ == "__main__":
    demonstrar_sistema_biblioteca()
    demonstrar_regras_negocio()