import json

from src.constants import TEST_KEYWORD, TEST_PAGE, SUPER_JOB_API_KEY
from src.site_discovers import HeadHunterDiscover, SuperJobDiscover


def test_get_request():
    hh = HeadHunterDiscover()
    sj = SuperJobDiscover()
    hh_params = {'text': TEST_KEYWORD, 'page': TEST_PAGE}
    sj_headers = {'X-Api-App-Id': SUPER_JOB_API_KEY}
    sj_params = {'keywords': TEST_KEYWORD, 'page': TEST_PAGE}
    assert isinstance(json.loads(hh.get_request(hh_params).text), dict)
    assert isinstance(json.loads(sj.get_request(sj_headers, sj_params).text), dict)
