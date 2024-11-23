"""
Define constantes baseadas nos caminhos do sistema de arquivos, 
facilitando o acesso a diretórios e arquivos frequentemente utilizados no projeto.

Constantes:
- FILE_PATH: Caminho absoluto do arquivo atual.
- PROJECT_PATH: Caminho absoluto da raiz do projeto.
- LOG_FOLDER_PATH: Caminho absoluto da pasta de logs.
- SRC_FOLDER_PATH: Caminho absoluto da pasta de código-fonte.
- CORE_FOLDER_PATH: Caminho absoluto da pasta 'core' dentro da pasta de código-fonte.
- LOG_FILE_PATH: Caminho absoluto do arquivo de logs.
- DOCS_YAML_FILE_PATH: Caminho absoluto do arquivo YAML contendo as docstrings.
- DOCSTRINGMANAGER_FILE_PATH: Caminho absoluto do arquivo 'docstringmanager.py'.
- TEST_FILE_PATH: Caminho absoluto do arquivo 'test.py'.
"""
from pathlib import Path

# Atribui as constantes raízes
FILE_PATH = Path(__file__).resolve()
PROJECT_PATH = FILE_PATH.parents[2]

# Atribui as constantes de pastas
LOG_FOLDER_PATH = PROJECT_PATH / 'logs'
SRC_FOLDER_PATH = PROJECT_PATH / 'src'
CORE_FOLDER_PATH = SRC_FOLDER_PATH / 'core'

# Atribui as constantes de arquivos
LOG_FILE_PATH = LOG_FOLDER_PATH / 'app.log'
DOCS_YAML_FILE_PATH = SRC_FOLDER_PATH / 'docstringmanager.yaml'
DOCSTRINGMANAGER_FILE_PATH = SRC_FOLDER_PATH / 'docstringmanager.py'
TEST_FILE_PATH = SRC_FOLDER_PATH / 'test.py'