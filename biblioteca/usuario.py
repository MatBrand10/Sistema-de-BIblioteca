class Usuario:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self._emprestimos = []

    def get_nome(self):
        return self._nome

    def get_matricula(self):
        return self._matricula

    def get_emprestimos(self):
        return self._emprestimos

    def pode_emprestar(self):
        raise NotImplementedError

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self._emprestimos.remove(emprestimo)