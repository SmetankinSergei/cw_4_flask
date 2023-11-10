from enum import Enum


class State(Enum):
    """Отражает состояние приложения - тестовое или рабочее"""
    WORK = 0
    TEST = 1
