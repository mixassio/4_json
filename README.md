# Prettify JSON

This module uses an already ready formatting function
Works with a json-file downloaded from https://data.mos.ru/opendata/7710881420-magaziny-alkogolnye-napitki

# Quickstart

https://github.com/lubyagin/python-json-pprint

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

'Id': 'c875f9a4-99aa-43e2-a992-2f7f42e420af',
  'Number': 6},
 {'Cells': {'Address': 'Новопетровская улица, дом 16',
            'AdmArea': 'Северный административный округ',
            'ClarificationOfWorkingHours': None,
            'District': 'район Коптево',
            'IsNetObject': 'нет',
            'Name': 'Разливное пиво',
            'OperatingCompany': None,
            'PublicPhone': [{'PublicPhone': '(495) 450-50-51'}],
            'TypeService': 'реализация продовольственных товаров',
            'WorkingHours': [{'DayOfWeek': 'понедельник',
                              'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'вторник', 'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'среда', 'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'четверг', 'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'пятница', 'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'суббота', 'Hours': '09:00-22:00'},
                             {'DayOfWeek': 'воскресенье',
                              'Hours': '09:00-22:00'}],
            'geoData': {'coordinates': [37.522740265286885, 55.82726147101704],
                        'type': 'Point'},
            'global_id': 14939869},



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
