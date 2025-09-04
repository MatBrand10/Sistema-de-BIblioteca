from usuario import Usuario

class Aluno(Usuario):
    LIMITE_EMPRESTIMO = 3

    def pode_emprestar(self):
        return len(self._emprestimos) < Aluno.LIMITE_EMPRESTIMO