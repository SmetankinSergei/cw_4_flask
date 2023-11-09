import json

from src import constants, dao
from src.site_discovers import HeadHunterDiscover, SuperJobDiscover
from src.vacancy import Vacancy


class WorkSession:
    def __init__(self):
        self.__hh_discover = HeadHunterDiscover()
        self.__sj_discover = SuperJobDiscover()
        self.__vacancies = []
        self.__sources = {constants.HH: self.__hh_discover,
                          constants.SJ: self.__sj_discover}

    def get_vacancies(self, action, source_name, keyword, page=0, top_count=5):
        if action == 'all':
            self.__get_all_vacancies(source_name, keyword, page)
            return [vacancy.get_info() for vacancy in self.__vacancies]
        elif action == 'top':
            vacancies = self.__get_top_vacancies(source_name, keyword, int(page), int(top_count))
            return [vacancy.get_info() for vacancy in vacancies]
        elif action == 'save':
            return self.__save_vacancies(source_name, keyword, int(page))

    def __save_vacancies(self, source_name, keyword, page=0):
        self.__get_vacancies(source_name, keyword, page)
        if self.__vacancies:
            data = [vacancy.get_info() for vacancy in self.__vacancies]
            dao.save_to_json(data)

    def __get_all_vacancies(self, source_name, keyword, page=0):
        self.__get_vacancies(source_name, keyword, page)
        return self.__vacancies

    def __get_top_vacancies(self, source_name, keyword, page=0, top_count=5):
        self.__get_vacancies(source_name, keyword, page)
        vacancies = self.__compare_vacancies_by_salary()
        vacancies = vacancies[:top_count]
        return vacancies

    def __get_vacancies(self, source_name, keyword, page=0):
        source = self.__sources.get(source_name, self.__hh_discover)
        vacancies = source.get_request(keyword, page)
        vacancies = json.loads(vacancies.text)[constants.ITEMS_NAMES[source_name]['vacancies']]
        self.__vacancies = [self.__create_vacancy(vacancy, source_name) for vacancy in vacancies]
        self.__vacancies = [vacancy for vacancy in self.__vacancies if vacancy is not None]

    def __compare_vacancies_by_salary(self):
        vacancies = [vacancy for vacancy in self.__vacancies if vacancy.salary is not None]
        vacancies = sorted(vacancies, key=lambda x: x.salary, reverse=True)
        return vacancies

    @staticmethod
    def __create_vacancy(vacancy, source_name):
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
