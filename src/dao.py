import json

from src.constants import PATH_TO_JSON


def save_to_json(vacancies):
    data = json.dumps(vacancies)
    with open(PATH_TO_JSON, 'w') as file:
        file.write(data)
