from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import (GetModelsData, CreateModelsData, RetrieveUpdateDestroyData, ExportXLSXandCSV)


urlpatterns = [
    path('api/list/<str:model_name>/', GetModelsData.as_view(), name='country-list'),  # Просмотр записей модели 
    path('api/create/<str:model_name>/', CreateModelsData.as_view(), name='country-create'),  # Создание записи модели 
    path('api/rud/<str:model_name>/<int:pk>/', RetrieveUpdateDestroyData.as_view(), name='country-refresh/delete'),  # Просмотр, обновление и удаление записи модели 
    path('api/export/<str:model_name>/<str:format>/', ExportXLSXandCSV.get, name='export_data'), # Экспорт данных в форматах xlsx или csv модели 
    path('api/token/', obtain_auth_token) 
]
