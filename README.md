⚠️ Nota: Este arquivo README.md está em construção. Algumas informações podem estar incompletas ou imprecisas no momento, e serão atualizadas conforme o projeto evolui.

# py-docstring-manager

Um utilitário para manipular docstrings em scripts Python, usando arquivos YAML como fonte de mapeamento. Facilita a adição, atualização e remoção de docstrings de forma programática, preservando o formato original do código.

---

## **Objetivo**

O objetivo principal do `py-docstring-manager` é auxiliar em cenários onde docstrings precisam ser gerenciadas dinamicamente, como:
- **Automação da documentação**: Geração ou atualização de docstrings de forma programática.
- **Padronização em larga escala**: Aplicação de um formato unificado em docstrings de projetos extensos.
- **Limpeza de código**: Remoção de docstrings desnecessárias ou redundantes.

---

## **Funcionalidades**

### 1. **Adicionar Docstrings**
A função `add_docstrings_from_yaml` permite:
- Inserir docstrings em funções e classes de um script Python.
- Substituir docstrings existentes por novos conteúdos definidos em um arquivo YAML.

### 2. **Remover Docstrings**
A função `remove_docstrings` oferece:
- Remoção de docstrings específicas, conforme definido em um arquivo YAML.
- Remoção de **todas** as docstrings de um script, caso nenhum arquivo YAML seja fornecido.

### 3. **Log de Operações**
- Ações como adição ou remoção de docstrings são registradas no log para maior visibilidade e controle.

---

## **Características Técnicas**

- **Preservação de Formato**: Utiliza a biblioteca `RedBaron` para manipular a árvore de sintaxe abstrata (AST) do código, garantindo que comentários, indentação e formatação original sejam preservados.
- **Configuração Baseada em YAML**: Um arquivo YAML fornece o mapeamento entre funções/classes e suas respectivas docstrings.
- **Simples e Extensível**: Projetado para facilitar a integração com outros scripts ou pipelines automatizados.

---

## **Exemplo de Arquivo YAML**

O arquivo YAML usado para adicionar docstrings deve seguir esta estrutura:

```yaml
functions:
  function: |
    Esta é a docstring da função `minha_funcao`.
    Inclui múltiplas linhas.

  other_function: |
    Docstring para a função `outra_funcao`.
    Inclui múltiplas linhas.

classes:
  MyClass: |
    Docstring da classe `MinhaClasse`.
```
## **Exemplo de Uso**

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

## **teste**

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/py-docstring-manager.git
cd py-docstring-manager
pip install -r requirements.txt
```


## Estrutura

```bash
PY-DOCSTRING-MANAGER/
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

