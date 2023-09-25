from django.db.models import *
from django.utils import timezone
import random

class People(Model):
    passport_number = BigIntegerField(primary_key=True)     
    first_name = CharField(max_length=255, null=False)
    second_name = CharField(max_length=255, null=False)
    phone_number = BigIntegerField(null=True)
    password = CharField(max_length=12,null=False,default='0')

    class Meta:
        """ Установка названия таблицы """
        db_table = 'People'

    def __str__(self):
        return str({'passport_number': self.passport_number, 'first_name': self.first_name,'second_name': self.second_name,'phone_number': self.phone_number,'password':self.password})

class Flat(Model):
    id = IntegerField(primary_key=True)
    type = CharField(max_length=255, null=True)
    area = IntegerField(null=True)
    password = CharField(null=False,max_length=12)
    humidity = DecimalField(null=False,max_digits=5,decimal_places=1,default=50.0)
    temperature = DecimalField(null=False,max_digits=5,decimal_places=1,default=30.0)

    class Meta:
        db_table = 'Flat'

    def __str__(self):
        return str({'id': self.id, 'type': self.type,'area': self.area,'password': self.password,'humidity': self.humidity,'temperature' : self.temperature})


class Access(Model):
    """ Таблица с наименованиями населённых пунктов """
    id = AutoField(primary_key=True)
    passport_number=ForeignKey('People', null=False, on_delete=CASCADE)
    flat_id=ForeignKey('Flat', null=False, on_delete=CASCADE)
    date = DateTimeField(auto_now=True,null=True) 
    condition=CharField(max_length=255, null=False)
    reason=CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'Access'
   
    def getFlatId(self):
        return self.flat_id

    def getPassport(self):
        return self.passport_number    

    def __str__(self):
        return str({'id': self.id, 'passport_number': self.passport_number,'flat_id': self.flat_id,'date': self.date,'condition': self.condition,'reason': self.reason})
