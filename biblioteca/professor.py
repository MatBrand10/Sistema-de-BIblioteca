from usuario import Usuario

class Professor(Usuario):
    LIMITE_EMPRESTIMO = 5

    def pode_emprestar(self):
        return len(self._emprestimos) < Professor.LIMITE_EMPRESTIMO