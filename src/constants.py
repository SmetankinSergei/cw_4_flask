import os.path

from src.session_actions import SessionActions
from src.vacancy import Vacancy

SUPER_JOB_API_KEY = 'v3.r.14216812.e35a2982d38760093d08dff919349fab3d562f98.8a79d5d5f172c17a070222e85ad5b899893db71c'

HH = 'hh'
SJ = 'sj'

ITEMS_NAMES = {HH: {'vacancies': 'items',
                    'name': 'name',
                    'url': 'url',
                    'salary': 'salary',
                    'requirements': 'snippet'},
               SJ: {'vacancies': 'objects',
                    'name': 'profession',
                    'url': 'link',
                    'salary': 'payment_from',
                    'requirements': 'candidat'}}

PATH_TO_JSON = os.path.join('..', 'data', 'data.json')
PATH_TO_TEST_JSON = os.path.join('tests', 'data.json')

TEST_VACANCIES = [
    {'name': 'Backend разработчик',
     'salary': 10000000,
     'url': 'https://api.hh.ru/vacancies/89109632?host=hh.ru',
     'requirements': 'Коммерческий опыт работы разработки Django на МИКРОСЕРВИСАХ не менее 5 лет обязательно; '
                     '(кандидаты без опыта не рассматриваются). Опыт работы с...'},
    {'name': 'QA Engineer Manual (Web)',
     'salary': 120000,
     'url': 'https://api.hh.ru/vacancies/88077138?host=hh.ru',
     'requirements': 'Опыт автоматизации тестирования, работы с различными фреймворками (Espresso, Appium,...). '
                     'Знание языков программирования (Java, <highlighttext>Python</highlighttext>, Bash) на уровне, '
                     'достаточном для написания...'},
    {'name': 'Системный администратор',
     'salary': 80000,
     'url': 'https://api.hh.ru/vacancies/89190586?host=hh.ru',
     'requirements': 'Опыт работы с IP телефонией (FreePBX на базе Asterisk). '
                     'Опыт администрирования СУБД - MSSQL, MySQL, PostgreSQL. '
                     'Умение писать скрипты (bash, <highlighttext>python</highlighttext>...'}]

TEST_CHECKS_DATA_OK = ['hh', 'Python', '3', '2']
TEST_CHECKS_DATA_FAIL_NUMS = ['hh', 'Python', 'a', 'b']
TEST_CHECKS_DATA_FAIL_SOURCE = ['aa', 'Python', '3', '2']
TEST_CHECKS_DATA_FAIL_KEYWORD = ['hh', '', '3', '2']

TEST_KEYWORD = 'Python'
TEST_PAGE = 3

TEST_VACANCY = Vacancy('Python developer', 'https://py_dev.com', 1000000, 'Full stack')
TEST_VACANCY_INFO = {
                    'name': 'Python developer',
                    'salary': 1000000,
                    'url': 'https://py_dev.com',
                    'requirements': 'Full stack'
                    }

SESSION_ACTIONS = {'all': SessionActions.ALL,
                   'top': SessionActions.TOP,
                   'save': SessionActions.SAVE}
