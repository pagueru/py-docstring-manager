from docstringmanager import add_docstrings_from_yaml, remove_docstrings
from core.constants import DOCS_YAML_FILE_PATH, TEST_FILE_PATH
from core.logger import logger


def main(chosen_example: int = 1):
    # Exemplo 1: Adiciona docstrings a um arquivo Python a partir de um arquivo YAML
    if chosen_example == 1:
        logger.info('Adicionando docstrings...')
        add_docstrings_from_yaml(TEST_FILE_PATH, DOCS_YAML_FILE_PATH)
       
    # Exemplo 2: Remove docstrings de arquivo Python a partir de um arquivo YAML 
    if chosen_example == 2:
        logger.info('Removendo docstrings...')
        remove_docstrings(TEST_FILE_PATH, DOCS_YAML_FILE_PATH)

    # Exemplo 3: Remove todas as docstrings de um arquivo Python
    if chosen_example == 3:
        logger.info('Removendo todas as docstrings...')
        remove_docstrings(TEST_FILE_PATH)

    # Exibe mensagem de conclusão
    if chosen_example:
        logger.info('Operações concluídas. Verifique o arquivo atualizado.')
    else:
        logger.info('Escolha um exemplo de uso.')

if __name__ == '__main__':
    # Seleciona o exemplo de uso
    main(1)