import json
import time
import random
import json
from locust import HttpUser, task, tag, between


# Статичные данные для тестирования
flat_types = ['one-room', 'two-room', 'three-room']
flat_ids= [8,22,34,39,40,50,51]

class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Адрес, к которому клиенты (предположительно) обращаются в первую очередь (это может быть индексная страница, страница авторизации и т.п.)
    def on_start(self):
        self.client.get("/api/docs")    # базовый класс HttpUser имеет встроенный HTTP-клиент для выполнения запросов (self.client)

    @tag("get_one_task")
    @task(3)
    def get_one_task(self):
        """ Тест GET-запроса """
        access_id = random.randint(14, 21)      # генерируем случайный id в диапазоне [4, 6]     
        with self.client.get(f'/api/access/{access_id}',        # тест get-метода, получение данных о доступе в квартиру
                             catch_response=True,
                             name='/api/access/{access_id}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("get_all_task")
    @task(10)
    def get_all_task(self):
        """ Тест GET-запроса (получение одной записи) """
        flat_type_id = random.randint(0,2)
        flat_type=flat_types[flat_type_id]
        with self.client.get(f'/api/flat/{flat_type}',
                             catch_response=True,
                             name='/api/flat/{flat_type}') as response:
            # Если получаем код HTTP-код 200 или 204, то оцениваем запрос как "успешный"
            if response.status_code == 200 or response.status_code == 204:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_task")
    @task(3)
    def put_task(self):
        """ Тест PuT-запроса (создание записи о погоде) """
        # Генерируем случайные данные в опредленном диапазоне
        chislo = random.randint(0,10)
        test_data = {'id': random.randint(14,21),
                     'passport_number':8020222222,
                     'flat_id':22,
                     'date': "2022-10-19 20:03:17.575562",
                     "condition": "OpenToday",
                     "reason": "BIG REASON Today"
                     }
        put_data = json.dumps(test_data)       # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.put('/api/access',
                              catch_response=True,
                              name='/api/access', data=put_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_task_flat")
    @task(1)
    def put_task(self):
        """ Тест PuT-запроса (создание записи о погоде) """
        # Генерируем случайные данные в опредленном диапазоне
        chislo = random.randint(0,6)
        flat_id=flat_ids[chislo]
        test_data = {'id': flat_id,
                     'type':"one",
                     'area':1,
                     'password': "1",
                     "humidity": random.randint(300,600)/10,
                     "temperature": random.randint(150,300)/10
                     }
        put_data = json.dumps(test_data)       # сериализуем тестовые данные в json-строку
        print(put_data)
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.put('/api/flat',
                              catch_response=True,
                              name='/api/flat', data=put_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_task")
    @task(1)
    def post_task(self):
        """ Тест PosT-запроса (обновление записи о погоде) """
        test_data = {'passport_number': random.randint(8000000000, 8999999999),
                     'first_name': "EdikTest",
                     'second_name': "DaukaevTest",
                     'phone_number': random.randint(89000000000, 89999999999),
                     'password':random.randint(100,1000)
                     }
        post_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.post('/api/people',
                             catch_response=True,
                             name='/api/people',
                             data=post_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

