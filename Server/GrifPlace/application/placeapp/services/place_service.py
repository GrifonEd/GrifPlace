from ..serializers import PeopleSerializer, FlatSerializer,AccessSerializer,AccessSerializer1,AccessSerializer2
from .repository_service import *


"""

    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    а также выполнение дополнительных операций над сериализаторами (если необходимо).

    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).
"""


class PlaceService:

    def get_people_by_id(self, id: int) -> Optional[PeopleSerializer]:
        result = get_people_by_passport(id)
        if result is not None:
            return PeopleSerializer(result)
        return result

    def get_all_flat_by_type(self, type: str) -> FlatSerializer:
        result = get_flat_by_type(type)
        flat_data = FlatSerializer(result, many=True)     # для возвращения списка объектов, необходимо создание сериализатора с аргументом many=True
        return flat_data

    def get_flat_by_id(self, id: int) -> Optional[FlatSerializer]:
        result = get_flat_by_id(id)
        if result is not None:
            return FlatSerializer(result)
        return result

    def get_access_in_id(self, id: int) -> AccessSerializer1:
        result = get_access_by_id(id)
        if result is not None:
            return AccessSerializer1(result)
        return result

    def get_access_by_people(self, passport: int) -> AccessSerializer2:
        result = get_access_by_pasport(passport)
        for flat_id in result:
            FlatSerializer(flat_id)
        if result is not None:
            return AccessSerializer2(result, many = True)
        return result

    def get_all_flats(self) -> FlatSerializer:
        result = get_all_flat()
        print(result)
        flat_data = FlatSerializer(result, many=True)     # для возвращения списка объектов, необходимо создание сериализатора с аргументом many=True
        return flat_data    
        

    def add_new_people(self, people: PeopleSerializer) -> None:
        print(people)
        people_data = people.data     # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        create_people(passport_number=people_data.get('passport_number'),
                       first_name=people_data.get('first_name'),
                       second_name=people_data.get('second_name'),
                       phone_number=people_data.get('phone_number'),
                       password = people_data.get('password')
                       )

    def add_new_access(self, access:AccessSerializer) -> None:
        access_data = access.data     # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        create_access(get_people_by_passport(passport_number=access.data.get('passport_number')),
                       get_flat_by_id(id=access.data.get('flat_id'))
        )

    def add_new_flat(self, flat: FlatSerializer) -> None:
        flat_data = flat.data     # получаем валидированные с помощью сериализатора данные (метод .data  возвращает объект типа dict)
        print(flat_data)
        create_flat(id=flat_data.get('id'),
                       type=flat_data.get('type'),
                       area=flat_data.get('area'),
                       password=flat_data.get('password'),
                       humidity=flat_data.get('humidity'),
                       temperature=flat_data.get('temperature')
                       )
        
    def update_flat_info(self, flat: FlatSerializer) -> None:
        flat_data = flat.data
        return update_flat_temp(temperature=flat_data.get('temperature'),
                                                humidity=flat_data.get('humidity'),
                                                id = flat_data.get('id')
                                                )

    def update_access_info(self, access: AccessSerializer) -> None:
        access_data = access.data
        return update_access_condition(condition=access_data.get('condition'),
                                                reason=access_data.get('reason'),
                                                id = access.data.get('id')
                                                )

    def update_access_info1(self, access: AccessSerializer) -> None:
        access_data = access.data
        print(access_data)
        return update_access_condition1(passport=access_data.get('passport_number'),
                                                flat = access.data.get('flat_id'),
                                                condition=access_data.get('condition'),
                                                reason=access_data.get('reason'),
                                                
                                                )

    def delete_people(self, passport_number: int) -> None:
        delete_people_by_passport(passport_number)

    def delete_access_info(self, id: int) -> None:
        delete_access_by_id(id)

    def delete_flat_info_by_type(self, type: str) -> None:
        delete_flat_by_type(type)

