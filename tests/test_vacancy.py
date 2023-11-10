from src.constants import TEST_VACANCY, TEST_VACANCY_INFO


def test_salary():
    assert TEST_VACANCY.salary == TEST_VACANCY_INFO['salary']


def test_get_info():
    assert TEST_VACANCY.get_info() == TEST_VACANCY_INFO
