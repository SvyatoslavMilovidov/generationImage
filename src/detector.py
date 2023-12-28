'''Модуль для запуска работы программы'''

import sys
import os
import argparse

from pathlib import Path
from loader import DETECTOR

def create_parser():
    '''Функция для парсинга аргументов терминала'''
    parser = argparse.ArgumentParser()
    parser.add_argument ('--source', default='00001.png')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    file_path = Path(*namespace.source.split(os.sep))
    img_extensions = ['.jpg', '.png']
    move_extensions = ['.mp4']
    

    assert file_path.suffix, 'Укажите расширение файла'
    assert file_path.suffix in (img_extensions + move_extensions), 'Выбранное расширение не поддерживается'

    if file_path.suffix in img_extensions:
        DETECTOR.get_predict_for_img(file_path)
    elif file_path.suffix in move_extensions:
        DETECTOR.get_predict_for_move(file_path)