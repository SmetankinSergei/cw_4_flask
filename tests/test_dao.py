from src import app_state
from src.constants import TEST_VACANCIES, PATH_TO_TEST_JSON
from src.dao import DAO


def test_save_to_json():
    dao = DAO(app_state.State.TEST)
    dao.save_to_json(TEST_VACANCIES)
    with open(PATH_TO_TEST_JSON) as file:
        vacancies = file.readlines()
        assert isinstance(vacancies, list)
        assert isinstance(vacancies[0][0], str)
