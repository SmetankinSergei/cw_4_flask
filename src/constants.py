import os.path

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
