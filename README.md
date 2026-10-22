# Sistema de Gerenciamento de Biblioteca

**Desenvolvido por:** Anna Victória Domingos Dantas

## Sobre o Projeto
Este projeto é um Sistema de Gerenciamento de Biblioteca desenvolvido para a avaliação de Linguagens de Programação. A aplicação integra Programação Orientada a Objetos (POO) e Programação Funcional (PF), garantindo o uso de funções puras, imutabilidade e operações de alta ordem. Não é utilizado banco de dados, sendo as informações mantidas em memória durante a execução.

## Linguagem Utilizada
- Python 3

## Funcionalidades Implementadas
- **Gestão de Acervo:** Cadastro de livros (identificador, título, autor e categoria).
- **Gestão de Usuários:** Cadastro de usuários (identificador, nome e matrícula).
- **Controlo de Empréstimos:** Registro de novos empréstimos (associando um livro a um único usuário) e devoluções.
- **Cálculo de Multas:** Função pura que calcula o valor da multa (R$ 2,00 por dia de atraso).
- **Filtros Funcionais:** Filtragem de livros por categoria utilizando `filter` sem alterar a coleção original.
- **Relatório de Multas (PF):** Geração de relatório de empréstimos ativos e atrasados utilizando obrigatoriamente `filter`, `map` e `reduce`.
- **Estatísticas (PF):** Agrupamento e contagem de livros por categoria utilizando `reduce`.
- **Comparação de Paradigmas:** Implementação de uma mesma funcionalidade de forma imperativa (laços de repetição) e funcional (funções de alta ordem).

## Instruções de Execução

1. Certifique-se de ter o Python instalado na sua máquina.
2. Faça o download ou clone este repositório contendo o arquivo `biblioteca.py`.
3. Abra o terminal (Prompt de Comando, PowerShell ou terminal do VS Code).
4. Navegue até a pasta onde o arquivo `biblioteca.py` está guardado.
5. Execute o seguinte comando:
   ```bash
   python biblioteca.py
