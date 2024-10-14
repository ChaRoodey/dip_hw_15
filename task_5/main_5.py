import os
from argparse import ArgumentParser
import logging
from collections import namedtuple


FORMAT = ''

def get_files(path: str):

    if not os.path.isdir(path):
        raise ValueError('Указанный путь не является директорией')

    file_info = namedtuple('file_info', ['type', 'name', 'extension', 'root_dir'])

    for root, dirs, files in os.walk(path):
        for dirr in dirs:
            new_dir = file_info('dir', dirr, None, os.path.basename(root))
            logging.info(f'{new_dir.type:<5}, {new_dir.name:<35}, {new_dir.root_dir:<21}, {new_dir.extension}')

        for file in files:
            if '.' in file:
                file_name = file.rsplit('.', 1)[0]
                file_extension = file.rsplit('.', 1)[1]
            else:
                file_name = file
                file_extension = None

            new_file = file_info('file', file_name ,file_extension , os.path.basename(root))
            logging.info(f'{new_file.type:<5}, {new_file.name:<35}, {new_file.root_dir:<21}, {new_file.extension}')

def main():
    logging.basicConfig(filename='dirs_log.log', style='{', level=logging.INFO, filemode='w', format=FORMAT)
    logging.info(f'type |                name                |        root_dir       | extension')

    parser = ArgumentParser(description='Сбор информации о всех вложенных файлах и деректориях и запись в лог')
    parser.add_argument('path',metavar='N', type=str, help='Путь к директории')
    args = parser.parse_args()

    try:
        get_files(args.path)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
