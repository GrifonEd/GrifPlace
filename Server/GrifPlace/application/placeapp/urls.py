from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from . import views

"""
    Подключение URI для приложения placeapp.
    Корневые URI представлены в базовом модуле application/urls.py
"""

# Метаданные Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Place Forecast API",
      default_version='v1',
      description="Place Forecast API",
      terms_of_service="https://example.com",
      contact=openapi.Contact(email="contact@mail.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('flat/<str:type>', views.GetDelAllFlat.as_view()),
    path('flat', views.PostFlat.as_view()),
    path('docs', views.Docs.as_view()),
    path('allflat', views.GetAllFlat.as_view()),
    path('accesspeopleflat', views.GetPeopleFlatAccess.as_view()),
    path('access', views.GetPostPutAccess.as_view()),
    path('accesspeople/<int:passport>', views.GetAccessByPeople.as_view()),
    path('access/<int:id>', views.GetAccess.as_view()),
    path('people', views.GetPostPeople.as_view()),
    path('people/<int:passport_number>', views.DelPeople.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
