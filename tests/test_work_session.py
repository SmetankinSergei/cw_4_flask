from src import app_state
from src.constants import PATH_TO_TEST_JSON
from src.dao import DAO
from src.work_session import WorkSession
"""В интернете холивар по поводу тестов приватных методов. В Java кто-то делает через рефлексию, тут, я думаю, 
можно через искажение имён, но я придерживаюсь мнения, что тестировать нужно публичные методы всё же, и как показали 
изыскания в сети, это самое распространённое мнение"""


def test_get_vacancies():
    dao = DAO(app_state.State.TEST)
    ws = WorkSession(dao)
    ws.get_vacancies('save', 'hh', 'Python', 3, 2)
    with open(PATH_TO_TEST_JSON) as file:
        vacancies = file.readlines()
        assert isinstance(vacancies, list)
        assert isinstance(vacancies[0][0], str)

    vacancies = ws.get_vacancies('all', 'hh', 'Python', 3, 2)
    assert isinstance(vacancies, list)
    vacancies = ws.get_vacancies('top', 'hh', 'Python', 3, 2)
    assert isinstance(vacancies, list)
