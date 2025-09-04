# Relatório de Modelagem – Sistema de Gerenciamento de Biblioteca

## 1. Herança entre Usuário, Aluno e Professor
Utilizamos herança para evitar duplicação de código. A classe `Usuario` representa todos os atributos e métodos comuns (nome, matrícula, lista de empréstimos). `Aluno` e `Professor` herdam de `Usuario` e implementam suas próprias regras de limite de empréstimos, usando polimorfismo no método `pode_emprestar()`.

## 2. Encapsulamento
Atributos das classes foram definidos como privados (prefixados com `_`), acessados por métodos getters/setters. Isso protege a integridade dos dados e garante que regras de negócio sejam respeitadas ao manipular empréstimos, livros e usuários.

## 3. Polimorfismo
O método `pode_emprestar()` é sobrescrito em `Aluno` e `Professor`. Assim, ao chamar `usuario.pode_emprestar()`, o sistema executa a regra correta conforme o tipo do usuário, sem precisar saber explicitamente se é aluno ou professor.

## 4. Associações e Regras
A classe `Emprestimo` associa um usuário a um livro, com datas de retirada e devolução. Cada usuário possui uma lista de empréstimos ativos. As funções de serviço garantem que as regras (limites, disponibilidade) sejam cumpridas.

## 5. Considerações
A modelagem favorece a expansão futura (ex: adicionar multa, reservas) e facilita manutenção. Encapsulamento, herança e polimorfismo tornam o código mais seguro, flexível e aderente à orientação a objetos.