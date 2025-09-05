from aluno import Aluno
from professor import Professor
from livro import Livro
from servicos import emprestar_livro, devolver_livro, relatorio_emprestimos

aluno1 = Aluno("Matheus", "2021001")
prof1 = Professor("Dua", "P1001")

livro1 = Livro("POO para Iniciantes", "Autor X")
livro2 = Livro("Python Essencial", "Autor Y")

usuarios = [aluno1, prof1]
livros = [livro1, livro2]

emprestar_livro(aluno1, livro1)
emprestar_livro(prof1, livro2)

for i in range(3):
    emprestar_livro(aluno1, Livro(f"Livro Extra {i}", "Autor Teste"))

# Devolver livro
devolver_livro(aluno1, livro1)

# Relatório
relatorio_emprestimos(usuarios)
