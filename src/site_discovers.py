from abc import ABC, abstractmethod
import os

import requests

from src.constants import SUPER_JOB_API_KEY


class SiteDiscover(ABC):
    """Абстрактный класс, в конкретно этом случае нужен только для определения интерфейса"""

    @abstractmethod
    def get_request(self, keyword, page=0):
        """Вот этого интерфейса - получение ответа от сервера"""
        pass


class HeadHunterDiscover(SiteDiscover):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_request(self, keyword, page=0):
        params = {'text': keyword, 'page': page}
        return requests.get(self.__url, params=params)


class SuperJobDiscover(SiteDiscover):
    def __init__(self):
        self.__url = 'https://api.superjob.ru/2.0/vacancies/'
        """Добавил строку с ключом из констант, чтобы можно было запустить приложение. 
        Закомментированная строка работает с ключом из переменной окружения"""
        # self.headers = {'X-Api-App-Id': os.environ['SUPER_JOB_API_KEY']}
        self.__headers = {'X-Api-App-Id': SUPER_JOB_API_KEY}

    def get_request(self, keyword, page=0):
        params = {'keywords': keyword, 'page': page}
        return requests.get(self.__url, headers=self.__headers, params=params)
