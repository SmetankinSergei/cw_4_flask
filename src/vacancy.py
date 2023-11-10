class Vacancy:
    """Класс для создания вакансий из данных"""
    def __init__(self, name, url, salary, requirements):
        self.__name = name
        self.__url = url
        self.__salary = salary
        self.__requirements = requirements

    def __repr__(self):
        return f'{__class__.__name__}: {self.__name}, salary: {self.__salary}, link: {self.__url}'

    @property
    def salary(self):
        """Геттер для зарплаты"""
        return self.__salary

    def get_info(self):
        """Получение подробной информации в виде словаря"""
        info = {
                'name': self.__name,
                'salary': self.__salary,
                'url': self.__url,
                'requirements': self.__requirements
                }
        return info
