from aluno import Aluno
from professor import Professor
from livro import Livro
from servicos import emprestar_livro, devolver_livro, relatorio_emprestimos

# Cadastro dos usuários
aluno1 = Aluno("João", "2021001")
prof1 = Professor("Maria", "P1001")

# Cadastro dos livros
livro1 = Livro("POO para Iniciantes", "Autor X")
livro2 = Livro("Python Essencial", "Autor Y")

usuarios = [aluno1, prof1]
livros = [livro1, livro2]

# Emprestar livros
emprestar_livro(aluno1, livro1)
emprestar_livro(prof1, livro2)

# Tentar ultrapassar o limite do aluno
for i in range(3):
    emprestar_livro(aluno1, Livro(f"Livro Extra {i}", "Autor Teste"))

# Devolver livro
devolver_livro(aluno1, livro1)

# Relatório
relatorio_emprestimos(usuarios)