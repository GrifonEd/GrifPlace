from typing import Optional, Iterable, List
from django.db.models import QuerySet
from ..models import People, Flat, Access
from ..serializers import PeopleSerializer, FlatSerializer,AccessSerializer,AccessSerializer1

def get_people_by_passport(passport_number: int) -> QuerySet:
    """ """
    people = People.objects.filter(passport_number=passport_number).first()
    return people


def get_flat_by_type(type: str) -> QuerySet:
    """ """
    flat = Flat.objects.filter(type=type).all()
    print(flat)
    return flat

def get_all_flat() -> QuerySet:
    """ """
    flat = Flat.objects.all()
    return flat

    
def get_flat_by_id(id: int) -> Optional[Flat]:
    """ """
    flat = Flat.objects.filter(id=id).first()
    return flat
    
def get_access_by_id(id: int) -> Optional[Access]:
    """ """
    access = Access.objects.filter(id=id).first()
    return access
    
def get_access_by_pasport(passport_number: int) -> QuerySet:
    """ """
    access = Access.objects.filter(passport_number=passport_number).all()
    return access

def get_access_by_passport_and_flat(passport_number: int,flat: int) -> QuerySet:
    access = Access.objects.filter(passport_number=passport_number).filter(flat_id=flat).first()
    return access

def create_people(passport_number: int, first_name: str, second_name: str, phone_number: int, password: str) -> None:
    """  """
    people = People.objects.create(passport_number=passport_number, first_name=first_name, second_name=second_name, phone_number=phone_number,password=password)
    people.save()
    
def create_flat(id: int, type: str, area: int,password: int,humidity:float,temperature:float) -> None:
    """ """
    flat = Flat.objects.create(id=id, type=type, area=area,password=password,humidity=humidity,temperature=temperature)
    print("Hmmmmmmmmmmmmmmmmm")
    print(flat)
    flat.save()
    
def create_access(passport_number: int, flat_id: int) -> None:
    """  """
    access = Access.objects.create(passport_number=passport_number, flat_id=flat_id,condition='Close',reason='No reason')
    access.save()

def update_access_condition(condition: str, reason: str, id: int) -> None:
    """  """
    access = get_access_by_id(id)
    access.condition = condition
    access.reason = reason
    access.save()

def update_flat_temp(temperature: float, humidity: float, id: int) -> None:
    """  """
    access = get_flat_by_id(id)
    access.temperature = temperature
    access.humidity = humidity
    access.save()

def update_access_condition1(condition: str, reason: str, passport: int, flat:int) -> None:
    """  """
    access = get_access_by_passport_and_flat(passport,flat)
    access.condition = condition
    access.reason = reason
    access.save()

def delete_access_by_id(id: int) -> None:
    """  """
    get_access_by_id(id).delete()

def delete_flat_by_id(id: int) -> None:
    """  """
    get_flat_by_id(id).delete()

def delete_flat_by_type(type: str) -> None:
    """  """
    get_flat_by_type(type).delete()

def delete_people_by_passport(passport_number: int) -> None:
    """  """
    get_people_by_passport(passport_number).delete()


