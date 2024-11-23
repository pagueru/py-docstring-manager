> [!IMPORTANT]  
> Este arquivo README.md está em construção. Algumas informações podem estar incompletas ou imprecisas no momento, e serão atualizadas conforme o projeto evolui.

# py-docstring-manager

O `py-docstring-manager` tem como objetivo centralizar o gerenciamento de docstrings em um arquivo YAML, oferecendo uma solução prática para projetos Python com scripts extensos. Ele ajuda a reduzir o tamanho do código durante o desenvolvimento e permite reintroduzir docstrings automaticamente para publicação ou compartilhamento do código com documentação completa.

### Principais Benefícios

- **Vantagens do YAML:** Oferece maior legibilidade, flexibilidade e é ideal para contextos onde a prioridade é a edição manual e intuitiva por humanos.

- **Redução do tamanho do script:** Remova as docstrings do código para simplificar o trabalho e torná-lo mais legível durante o desenvolvimento.

- **Publicação do código com documentação:** Adicione automaticamente as docstrings de volta ao script quando necessário, como para publicar o código com documentação completa.

- **Preservação do formato:** Garante que a formatação original seja mantida durante as operações.

- **aa:** 

---

## **Funcionalidades**

### 1. **Adicionar Docstrings**
A função `add_docstrings_from_yaml` permite:
- Inserir ou substituir docstrings em funções e classes de um script Python, utilizando os conteúdos definidos em um arquivo YAML.

### 2. **Remover Docstrings**
A função `remove_docstrings` possibilita:
- Remover docstrings específicas com base no mapeamento de um arquivo YAML.
- Remover todas as docstrings de um script, caso o arquivo YAML não seja fornecido.

---

## **Características**

- **Preservação de formato:** Utiliza a biblioteca `RedBaron` para manipular a árvore de sintaxe abstrata (AST - Abstract Syntax Tree) do código, garantindo que comentários, indentação e formatação original sejam preservados.

- **Controle centralizado:** O uso de YAML como fonte facilita a edição e atualização de docstrings fora do código.

- **Preservação do formato:** Utiliza RedBaron para manipular a AST (Abstract Syntax Tree), garantindo que a estrutura, os comentários e a formatação do código permaneçam intactos.

---

## **Exemplo de Arquivo YAML**

O arquivo YAML utilizado para adicionar docstrings (no exemplo, no estilo Google Style) deve seguir a estrutura abaixo:

```yaml
functions:
  function: |
    Faz algo interessante com os números fornecidos.

    Args:
        x (int): Um número inteiro.
        y (float): Um número decimal.

    Returns:
        float: O resultado da soma dos números fornecidos.

    Raises:
        ValueError: Se `x` for negativo.

  other_function: |
    Verifica se uma string é um palíndromo.

    Args:
        texto (str): A string a ser verificada.

    Returns:
        bool: True se a string for um palíndromo, False caso contrário.
    
classes:
  MyClass: |
    Representa uma entidade com atributos simples.

    Attributes:
        atributo1 (int): Um atributo inteiro.
        atributo2 (str): Um atributo textual.
```

## **Exemplo de Uso**

Na pasta `src` do projeto, você encontrará os seguintes arquivos:
- `docstringmanager.py`: Módulo principal que implementa as funcionalidades do projeto.
- `docstringmanager.yaml`: Arquivo YAML contendo o mapeamento de docstrings para funções e classes.
- `sample.py`: Script exemplo com funções e classes, algumas com docstrings e outras sem, para demonstração das operações.
- `usage_exemples.py`: Script que importa o módulo `docstringmanager.py` e executa exemplos, utilizando o arquivo `docstringmanager.yaml` para manipular docstrings no `sample.py`.

### Adicionar Docstrings a um Script Python

```python
from py_docstring_manager.core import add_docstrings_from_yaml

add_docstrings_from_yaml('meu_script.py', 'docstrings.yaml')
```
### Remover Docstrings de um Script Python

```python
from py_docstring_manager.core import remove_docstrings

# Remove todas as docstrings
remove_docstrings('meu_script.py')

# Remove apenas as docstrings definidas no YAML
remove_docstrings('meu_script.py', 'docstrings.yaml')
```

## Estrutura do Projeto

```bash
.
├── .venv/
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── logs/
│   └── app.log
├── src/
│   ├── core/
│   │   ├── docstringmanager.yaml
│   │   ├── sample.py
│   │   └── usage_examples.py
│   ├── docstringmanager.py
├── tools/
│   ├── commit.txt
│   ├── template_commit.txt
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CONTRIBUTING.md
├── poetry.lock
├── pyproject.toml
└── README.md
```

# Contato

GitHub: [pagueru](https://github.com/pagueru/)

LinkedIn: [Raphael Henrique Vieira Coelho](https://www.linkedin.com/in/raphaelhvcoelho/)

E-mail: [raphael.phael@gmail.com](mailto:raphael.phael@gmail.com)

