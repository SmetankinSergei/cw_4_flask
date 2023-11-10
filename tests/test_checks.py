from src.checks import check_data
from src.constants import TEST_CHECKS_DATA_OK, TEST_CHECKS_DATA_FAIL_NUMS, TEST_CHECKS_DATA_FAIL_SOURCE, \
    TEST_CHECKS_DATA_FAIL_KEYWORD


def test_check_data():
    assert check_data(*TEST_CHECKS_DATA_OK) is True
    assert check_data(*TEST_CHECKS_DATA_FAIL_NUMS) is False
    assert check_data(*TEST_CHECKS_DATA_FAIL_SOURCE) is False
    assert check_data(*TEST_CHECKS_DATA_FAIL_KEYWORD) is False
