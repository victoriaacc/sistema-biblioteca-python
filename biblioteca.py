from datetime import date
from functools import reduce

class Livro:
    def __init__(self, identificador, titulo, autor, categoria):
        self.identificador = identificador
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

class Usuario:
    def __init__(self, identificador, nome, matricula):
        self.identificador = identificador
        self.nome = nome
        self.matricula = matricula

class Emprestimo:
    def __init__(self, identificador, livro, usuario, data_emprestimo, data_prevista):
        self.identificador = identificador
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_prevista = data_prevista
        self.data_devolucao = None

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def registrar_emprestimo(self, emprestimo):
        livros_emprestados = [e.livro.identificador for e in self.emprestimos if e.data_devolucao is None]
        if emprestimo.livro.identificador not in livros_emprestados:
            self.emprestimos.append(emprestimo)

    def registrar_devolucao(self, identificador_emprestimo, data_devolucao):
        for emprestimo in self.emprestimos:
            if emprestimo.identificador == identificador_emprestimo and emprestimo.data_devolucao is None:
                emprestimo.data_devolucao = data_devolucao
                break

def calcular_multa(dias_atraso, valor_diaria=2.0):
    return dias_atraso * valor_diaria if dias_atraso > 0 else 0.0

def filtrar_livros_por_categoria(livros, categoria):
    return list(filter(lambda livro: livro.categoria == categoria, livros))

def filtrar_emprestimos_atrasados(emprestimos, data_referencia):
    return list(filter(lambda e: e.data_devolucao is None and (data_referencia - e.data_prevista).days > 0, emprestimos))

def relatorio_multas(emprestimos, data_referencia):
    atrasados = filter(lambda e: e.data_devolucao is None and (data_referencia - e.data_prevista).days > 0, emprestimos)
    multas = map(lambda e: calcular_multa((data_referencia - e.data_prevista).days), atrasados)
    return reduce(lambda acc, val: acc + val, multas, 0.0)

def estatistica_quantidade_livros_categoria(livros):
    return reduce(lambda acc, livro: {**acc, livro.categoria: acc.get(livro.categoria, 0) + 1}, livros, {})

def filtrar_livros_imperativo(livros, categoria):
    resultado = []
    for livro in livros:
        if livro.categoria == categoria:
            resultado.append(livro)
    return resultado
if __name__ == "__main__":
    biblioteca = Biblioteca()
    
    livro1 = Livro(1, "O Senhor dos Aneis", "J.R.R. Tolkien", "Fantasia")
    livro2 = Livro(2, "Clean Code", "Robert C. Martin", "Tecnologia")
    livro3 = Livro(3, "O Hobbit", "J.R.R. Tolkien", "Fantasia")
    
    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)
    biblioteca.cadastrar_livro(livro3)
    
    user1 = Usuario(1, "Ana Silva", "2023001")
    user2 = Usuario(2, "Carlos Souza", "2023002")
    
    biblioteca.cadastrar_usuario(user1)
    biblioteca.cadastrar_usuario(user2)
    
    hoje = date(2023, 10, 20)
    
    emp1 = Emprestimo(1, livro1, user1, date(2023, 10, 5), date(2023, 10, 15))
    emp2 = Emprestimo(2, livro2, user2, date(2023, 10, 10), date(2023, 10, 25))
    
    biblioteca.registrar_emprestimo(emp1)
    biblioteca.registrar_emprestimo(emp2)
    
    print("Multas totais:", relatorio_multas(biblioteca.emprestimos, hoje))
    
    livros_fantasia = filtrar_livros_por_categoria(biblioteca.livros, "Fantasia")
    print("Livros de Fantasia:", [l.titulo for l in livros_fantasia])
    
    print("Estatisticas:", estatistica_quantidade_livros_categoria(biblioteca.livros))