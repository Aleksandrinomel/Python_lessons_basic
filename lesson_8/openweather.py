
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import os
import sqlite3 as sql
import json
import requests
from datetime import datetime


path_dir = os.path.dirname(__file__)


def get_path_to_file(file_name, path_to_dir=path_dir):
    return os.path.join(path_to_dir, file_name)


with open(get_path_to_file("app.id"), encoding="utf-8") as f:
    app_id = f.readline().rstrip()


def check_city(country, city):
    with open(get_path_to_file("city.list.json")) as f:
        f_json = json.load(f)
        city_list = [x for x in f_json if x['country'] == country and x['name'] == city]
        print(city_list)
        if len(city_list) == 0:
            print("Не удалось найти город.")
            return None
        elif len(city_list) == 1:
            print("Город найден.")
            return request_city_weather(city_list[0]['id'])
        elif len(city_list) > 1:
            print(f"{_}" for _ in city_list)
            city_id = input("Уточните ваш город, введя его id из предложенных выше:")
            return request_city_weather(city_id)


def request_city_weather(city_id, appid=app_id):
    request = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={appid}'
    response = requests.get(request)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(f"Ответ сервера :{response.content}")
        return None


class WeatherDB:
    def __init__(self):
        self.db_name = "weather.db"
        self.create_db()
        self.sity_list_name = "city.list.json"

    def db_is_exists(self):
        return os.path.isfile(get_path_to_file(self.db_name))

    def create_db(self):
        if not self.db_is_exists():
            conn = sql.connect(os.path.join(get_path_to_file(self.db_name)))
            cursor = conn.cursor()

            cursor.execute("""CREATE TABLE "weather" (
                            `city_id`	INTEGER NOT NULL,
                            `city`	VARCHAR(255) NOT NULL,
                            `date`	DATE NOT NULL,
                            `temperature`	INTEGER NOT NULL,
                            `weather_id`	INTEGER NOT NULL,
                            PRIMARY KEY(`city_id`)
                        ); """)
            conn.commit()
            conn.close()

    def add_city_weather(self, json_response_content):
        if json_response_content:
            conn = sql.connect(os.path.join(get_path_to_file(self.db_name)))
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO weather VALUES (?,?,?,?,?)", [json_response_content['id'],
                                                                          json_response_content['name'],
                                                                          datetime.now().strftime('%Y-%m-%d'),
                                                                          json_response_content['main']['temp'],
                                                                          json_response_content['weather'][0]['id']
                                                                          ])
                print('Добавленно в базу')
            except sql.IntegrityError:
                cursor.execute(f'UPDATE weather SET temperature="{json_response_content["main"]["temp"]}",'
                               f' date="{datetime.now().strftime("%Y-%m-%d")}",'
                               f' weather_id="{json_response_content["weather"][0]["id"]}"'
                               f' WHERE city_id="{json_response_content["id"]}"')
                print("Температура обновлена")
            conn.commit()
            conn.close()

    @staticmethod
    def get_data():
        conn = sql.connect(os.path.join(get_path_to_file("weather.db")))
        cursor = conn.cursor()
        data = list(cursor.execute('select * from weather'))
        return data


def main():
    weather = WeatherDB()
    while True:
        country = input("Введите название страны. Например: 'RU'")
        city = input("Введите название города. Например: 'Moscow'")
        weather_data = check_city(country, city)
        if weather_data:
            weather.add_city_weather(weather_data)
        inp = input("Продолжить? (y/n)")
        if inp == 'n':
            break


if __name__ == '__main__':
    main()
