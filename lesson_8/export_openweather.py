
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
from openweather import WeatherDB as db
from openweather import get_path_to_file


def gen_csv(file_name):
    data = weather.get_data()
    with open(file_name, 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['city_id', 'city', 'date', 'temperature', 'weather_id'])
        for row in data:
            csv_out.writerow(row)


def gen_json(file_name):
    json_data = []
    data = weather.get_data()
    for row in data:
        json_data.append({'city_id': row[0], 'city': row[1], 'date': row[2], 'temperature': row[3], 'weather_id': row[4]})
    with open(file_name, 'w') as out:
        json.dump(json_data, out)


def gen_html(file_name):
    content = ''
    data = weather.get_data()
    for row in data:
        html_content = f"<div><b>{row[1]} </b><b> {row[3]} &deg;C </b><b> {row[2]} </b></div>"
        content += html_content

    html_template = f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Weather</title></head>' \
                    f'<body>{content}</body></html>'
    with open(file_name, 'w') as out:
        out.write(html_template)


if __name__ == '__main__':
    weather = db
    file_name = sys.argv[2] + '.' + sys.argv[1][2:]
    do = {'csv': gen_csv,
          'html': gen_html,
          'json': gen_json}

    if len(sys.argv) != 3:
        print("Указано неверное число аргументов")
        sys.exit()

    do[sys.argv[1][2:]](file_name)
    print("Файл создан")





