'''Модуль с описанием класса детектора'''

import cv2
import numpy as np

from PIL import Image
from pathlib import Path
from ultralytics import YOLO

class CigaretteDetector:
    """Класс TextSplitter используется для разбивки текста на слова 
    
    Основное применение - парсинг логов на отдельные элементы по указанному разделителю. 
    
    Note:
        Возможны проблемы с поиском пути к файлу
        
    Attributes: 
        model : YOLO экземпляр класса модели 
    
    Methods:
        get_predict_for_img() - отрисовывает bbox на изображении по указанному пути
        get_predict_for_move() - отрисовывает bbox на видео по указнному пути
    """

    def __init__(self, model: YOLO):
        self.model = model

    def get_predict_for_img(self, img_path: Path) -> None:
        '''
        Метод для детектирования изображения

        Args:
            img_path (Path): путь к изображению
        '''

        res = self.model(img_path)
        res_plotted = res[0].plot()

        imageRGB = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(imageRGB)
        img.save(img_path.name)

    def get_predict_for_move(self, move_path: Path) -> None:
        '''
        Метод для детектирования видео

        Args:
            file_name (Path): путь к видео
        '''
        
        # Берём видео и считываем основные параметры
        cap = cv2.VideoCapture(str(move_path))
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')

        # Создаем класс для записи
        out = cv2.VideoWriter(move_path.name, fourcc, fps, (width, height))

        #  Обрабатываем кадры
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame = self.model(frame)
                frame = frame[0].plot()
                out.write(frame)
            else:
                break
        cap.release()
        out.release()
