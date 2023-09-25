from django.test import TestCase
import random
from .services.repository_service import *

class TestPlaceRepositoryService(TestCase):

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        # создаем тестовые записи
        create_people(passport_number = 8010000000,first_name='Igor',second_name = 'Bobrov',phone_number=random.randint(89000000000,89999999999),password=1)
        create_flat(id=200,type='two-room',area=random.randint(40,80),password=123456789,humidity=34,temperature=10)
        create_flat(id=300,type='two-room',area=random.randint(40,80),password=987654321,humidity=11,temperature=43)
        create_access(get_people_by_passport(passport_number=8010000000), get_flat_by_id(id=200))

    def test_get_flat(self):
        """ Тест функции поиска квартиры по типу """
        flat_by_type = get_flat_by_type(type='two-room')
        peple_by_pasport = get_people_by_passport(passport_number=8010000000)
        print(peple_by_pasport,"\n")
        
        access_norm=get_access_by_pasport(peple_by_pasport)
        for row in access_norm:
            print(row)
        print("\n")
        for row in flat_by_type:
            print(row)
            self.assertIsNotNone(row)  # запись должна существовать
            self.assertTrue(row.type == 'two-room')  # идентификатор Type == 'two-room' (т.е. тип квартиры 'two-room' в таблице Type)
        print("\n")


    def test_delete_flat(self):
        """ Тест функции удаления квартиры по ID """
        print(get_flat_by_id(id=300),"\n")
        delete_flat_by_id(id=300)
        result = get_flat_by_id(id=300)  # ищем запись по ID квартиры 
        self.assertIsNone(result)  # запись не должна существовать


    def test_update_access(self):
        print(get_access_by_id(id=1))
        update_access_condition(condition='Open',reason='Norm_Reason',id=1)
        print(get_access_by_id(id=1))
     
    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        pass


