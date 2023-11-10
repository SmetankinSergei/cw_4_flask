import json

from src import app_state
from src.constants import PATH_TO_JSON, PATH_TO_TEST_JSON


class DAO:
    """Data Access Object: класс, который ходит в файлы, базы и тому подобные места"""
    def __init__(self, state_now):
        self.__state_now = state_now

    def save_to_json(self, vacancies):
        """Сохраняет данные в файл"""
        path = PATH_TO_JSON
        if self.__state_now == app_state.State.TEST:
            path = PATH_TO_TEST_JSON
        data = json.dumps(vacancies)
        with open(path, 'w') as file:
            file.write(data)
