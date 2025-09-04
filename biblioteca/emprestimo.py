from datetime import date, timedelta

class Emprestimo:
    def __init__(self, usuario, livro, dias_prazo=7):
        self._usuario = usuario
        self._livro = livro
        self._data_retirada = date.today()
        self._data_devolucao = self._data_retirada + timedelta(days=dias_prazo)

    def get_usuario(self):
        return self._usuario

    def get_livro(self):
        return self._livro

    def get_data_retirada(self):
        return self._data_retirada

    def get_data_devolucao(self):
        return self._data_devolucao