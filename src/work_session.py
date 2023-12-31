import json

from src import constants
from src.session_actions import SessionActions
from src.site_discovers import HeadHunterDiscover, SuperJobDiscover
from src.vacancy import Vacancy


class WorkSession:
    """Класс рабочей сессии. Рабочая сессия - для управления приложением"""
    def __init__(self, main_dao):
        self.__hh_discover = HeadHunterDiscover()
        self.__sj_discover = SuperJobDiscover()
        self.__vacancies = []
        self.__top_count = 0
        self.__dao = main_dao
        self.__sources = {constants.HH: self.__hh_discover,
                          constants.SJ: self.__sj_discover}
        self.__actions = {SessionActions.ALL: self.__get_all_vacancies,
                          SessionActions.TOP: self.__get_top_vacancies,
                          SessionActions.SAVE: self.__save_vacancies}

    def get_vacancies(self, action, source_name, keyword, page, top_count):
        """Единственный метод публичного интерфейса, управляющий приложением"""
        self.__top_count = int(top_count)
        return self.__actions[action](source_name, keyword, page)

    def __save_vacancies(self, source_name, keyword, page):
        """Сохранение данных в файл"""
        self.__get_vacancies(source_name, keyword, page)
        if self.__vacancies:
            data = [vacancy.get_info() for vacancy in self.__vacancies]
            self.__dao.save_to_json(data)

    def __get_all_vacancies(self, source_name, keyword, page):
        """Получение данных по всем вакансиям"""
        self.__get_vacancies(source_name, keyword, page)
        return [vacancy.get_info() for vacancy in self.__vacancies]

    def __get_top_vacancies(self, source_name, keyword, page, top_count=5):
        """Получение данных по самым высокооплачиваемым вакансиям"""
        self.__get_vacancies(source_name, keyword, page)
        vacancies = self.__compare_vacancies_by_salary()
        vacancies = vacancies[:self.__top_count]
        return [vacancy.get_info() for vacancy in vacancies]

    def __get_vacancies(self, source_name, keyword, page):
        """Создание вакансий из данных ответа сервера"""
        source = self.__sources.get(source_name, self.__hh_discover)
        vacancies = source.get_request(keyword, page)
        vacancies = json.loads(vacancies.text)[constants.ITEMS_NAMES[source_name]['vacancies']]
        self.__vacancies = [self.__create_vacancy(vacancy, source_name) for vacancy in vacancies]
        self.__vacancies = [vacancy for vacancy in self.__vacancies if vacancy is not None]

    def __compare_vacancies_by_salary(self):
        """Сортировка вакансий по убыванию зарплаты"""
        vacancies = [vacancy for vacancy in self.__vacancies if vacancy.salary is not None]
        vacancies = sorted(vacancies, key=lambda x: x.salary, reverse=True)
        return vacancies

    @staticmethod
    def __create_vacancy(vacancy, source_name):
        """Создание объекта вакансии из данных. Так как не было чёткого задания, каким образом это делать,
        я просто решил отсеивать все, где недостаточно данных для создания полностью заполненного шаблона,
        поэтому применил инструкцию except без указания конкретной проблемы, что позволяет приложению
        просто продолжить работу, если что-то пошло не так"""
        try:
            name = vacancy[constants.ITEMS_NAMES[source_name]['name']]
            url = vacancy[constants.ITEMS_NAMES[source_name]['url']]
            salary = vacancy[constants.ITEMS_NAMES[source_name]['salary']]
            requirements = vacancy[constants.ITEMS_NAMES[source_name]['requirements']]
            if source_name == constants.HH:
                salary = salary['from']
                requirements = requirements['requirement']
            return Vacancy(name, url, salary, requirements)
        except:
            pass
