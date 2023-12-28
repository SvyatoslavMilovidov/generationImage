'''Модуль для инциализации основных объектов'''

import const
from get_prediction import CigaretteDetector
from ultralytics import YOLO


MODEL = YOLO(const.MODEL_PATH)
DETECTOR = CigaretteDetector(MODEL)