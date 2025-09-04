from emprestimo import Emprestimo

def emprestar_livro(usuario, livro):
    if not livro.is_disponivel():
        print("Livro não disponível.")
        return None
    if not usuario.pode_emprestar():
        print("Usuário atingiu o limite de empréstimos.")
        return None
    emprestimo = Emprestimo(usuario, livro)
    usuario.adicionar_emprestimo(emprestimo)
    livro.emprestar()
    print(f"Empréstimo realizado: {usuario.get_nome()} -> {livro.get_titulo()}")
    return emprestimo

def devolver_livro(usuario, livro):
    for emp in usuario.get_emprestimos():
        if emp.get_livro() == livro:
            usuario.remover_emprestimo(emp)
            livro.devolver()
            print(f"Livro devolvido: {usuario.get_nome()} -> {livro.get_titulo()}")
            return True
    print("Empréstimo não encontrado.")
    return False

def relatorio_emprestimos(usuarios):
    print("Relatório de Livros Emprestados:")
    for usuario in usuarios:
        for emp in usuario.get_emprestimos():
            print(f"{emp.get_livro().get_titulo()} - {usuario.get_nome()} até {emp.get_data_devolucao()}")