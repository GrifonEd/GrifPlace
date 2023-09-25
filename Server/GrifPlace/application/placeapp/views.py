from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status


from .serializers import PeopleSerializer, FlatSerializer,AccessSerializer,AccessSerializer1
from .services.place_service import PlaceService
# Create your views here.

service = PlaceService()      # подключаем слой с бизнес-логикой


class GetDelAllFlat(GenericAPIView):
    serializer_class = FlatSerializer    # определяем сериализатор (необходимо для генерирования страницы Swagger)
    renderer_classes = [JSONRenderer]       # определяем тип входных данных

    def get(self, request: Request, type: str) -> Response:                                        #РАБОТАЕТ
        """ Получение всех записей квартир по типу """
        response = service.get_all_flat_by_type(type)
        return Response(data=response.data)

    def delete(self, request: Request, type: str) -> Response:                                        #РАБОТАЕТ
        """ Удаление всех записей квартир по типу """
        service.delete_flat_info_by_type(type)
        return Response(status=status.HTTP_200_OK)

class GetAllFlat(GenericAPIView):
    serializer_class = FlatSerializer    # определяем сериализатор (необходимо для генерирования страницы Swagger)
    renderer_classes = [JSONRenderer]       # определяем тип входных данных

    def get(self, request: Request) -> Response:                                        #РАБОТАЕТ
        """ Получение всех записей квартир по типу """
        response = service.get_all_flats()
        return Response(data=response.data)
    
class GetPeopleFlatAccess(GenericAPIView):
    serializer_class = AccessSerializer
    renderer_classes = [JSONRenderer]
        
    def post(self, request: Request, *args, **kwargs) -> Response:           # РАБОТАЕТ
        """ Добавить новую запись о доступе в квартиру """
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            service.add_new_access(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args, **kwargs) -> Response:   # Работает но передавать нужно все данные
        """ Обновить запись о доступе в квартиру """
        serializer = AccessSerializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():
            service.update_access_info1(serializer)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class GetAccessByPeople(GenericAPIView):
    serializer_class = AccessSerializer
    renderer_classes = [JSONRenderer]
        
    def get(self, request: Request, passport: int) -> Response:                                        
        """ Получение всех записей квартир по типу """
        response = service.get_access_by_people(passport)
        #print(FlatSerializer(response.flat_id))
        return Response(data=response.data)

class GetAccess(GenericAPIView):
    serializer_class = AccessSerializer
    renderer_classes = [JSONRenderer]
        
    def get(self, request: Request, id: int) -> Response:                                        
        """ Получение всех записей квартир по типу """
        response = service.get_access_in_id(id)
        return Response(data=response.data)

    def delete(self, request: Request,id: int) -> Response:                                        #РАБОТАЕТ
        """ Удаление всех записей квартир по типу """
        service.delete_access_info(id)
        return Response(status=status.HTTP_200_OK)

class PostFlat(GenericAPIView):
    serializer_class = FlatSerializer    # определяем сериализатор (необходимо для генерирования страницы Swagger)
    renderer_classes = [JSONRenderer]                                         #РАБОТАЕТ
    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить новую квартиру """
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            service.add_new_flat(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request: Request, *args, **kwargs) -> Response:   # Работает но передавать нужно все данные
        """ Обновить запись о доступе в квартиру """
        serializer = FlatSerializer(data=request.data)
        #print(serializer)
        if serializer.is_valid():
            service.update_flat_info(serializer)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

        
class Docs(GenericAPIView):
    renderer_classes = [JSONRenderer]

    def get(self, request: Request) -> Response:                                        
        docs = {
	"Status": 'Скоро будет'
}

        response = docs
        return Response(response)



class GetPostPutAccess(GenericAPIView):
    serializer_class = AccessSerializer
    renderer_classes = [JSONRenderer]



    def post(self, request: Request, *args, **kwargs) -> Response:           # РАБОТАЕТ
        """ Добавить новую запись о доступе в квартиру """
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            service.add_new_access(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args, **kwargs) -> Response:   # Работает но передавать нужно все данные
        """ Обновить запись о доступе в квартиру """
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            service.update_access_info(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        


class GetPostPeople(CreateAPIView):                                        #РАБОТАЕТ
    serializer_class = PeopleSerializer
    renderer_classes = [JSONRenderer]



    def post(self, request: Request, *args, **kwargs) -> Response:
        """ Добавить нового пользователя """
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            service.add_new_people(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DelPeople(CreateAPIView):                                        #РАБОТАЕТ
    serializer_class = PeopleSerializer
    renderer_classes = [JSONRenderer]

    def delete(self, request: Request,passport_number:int) -> Response:                                        #РАБОТАЕТ
        """ Удаление всех записей квартир по типу """
        service.delete_people(passport_number)
        return Response(status=status.HTTP_200_OK)


    def get(self, request: Request,passport_number:int) -> Response:                                        #РАБОТАЕТ
        """ Получение всех записей квартир по типу """
        response = service.get_people_by_id(passport_number)
        return Response(data=response.data)