from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (CountryListAPIView, CountryCreateAPIView, CountryRetrieveUpdateDestroyAPIView,
                    ManufacturerListAPIView, ManufacturerCreateAPIView, ManufacturerRetrieveUpdateDestroyAPIView,
                    CarListAPIView, CarCreateAPIView, CarRetrieveUpdateDestroyAPIView,
                    CommentsListAPIView,CommentsCreateAPIView, CommentsRetrieveUpdateDestroyAPIView,
                    ExportCountryDataXlsxView, ExportManufacturerDataXlsxView, ExportCarDataXlsxView, ExportCommentsDataXlsxView,
                    ExportCountryDataCSVView, ExportManufaturerDataCSVView, ExportCarDataCSVView, ExportCommentDataCSVView)



urlpatterns = [
    path('api/countries/', CountryListAPIView.as_view(), name='country-list'),  # Просмотр записей модели Country
    path('api/countries/create/', CountryCreateAPIView.as_view(), name='country-create'),  # Создание записи модели Country
    path('api/countries/<int:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-refresh/delete'),  # Просмотр, обновление и удаление записи модели Country

    path('api/cars/', CarListAPIView.as_view(), name='car-list'),  # Просмотр записей модели Car
    path('api/cars/create/', CarCreateAPIView.as_view(), name='car-create'),  # Создание записи модели Car
    path('api/cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='car-refresh/delete'),  # Просмотр, обновление и удаление записи модели Car

    path('api/manufacturers/', ManufacturerListAPIView.as_view(), name='manufacturer-list'),  # Просмотр записей модели Manufacturer
    path('api/manufacturers/create/', ManufacturerCreateAPIView.as_view(), name='manufacturer-create'),  # Создание записи модели Manufacturer
    path('api/manufacturers/<int:pk>/', ManufacturerRetrieveUpdateDestroyAPIView.as_view(), name='manufacturer-refresh/delete'),  # Просмотр, обновление и удаление записи модели Manufacturer

    path('api/comments/', CommentsListAPIView.as_view(), name='comment-list'),  # Просмотр записей модели Comment
    path('api/comments/create/', CommentsCreateAPIView.as_view(), name='comment-create'),  # Создание записи модели Comment
    path('api/comments/<int:pk>/', CommentsRetrieveUpdateDestroyAPIView.as_view(), name='comment-refresh/delete'),  # Просмотр, обновление и удаление записи модели Comment

    path('api/countires/xlsx/', ExportCountryDataXlsxView.as_view(), name='xlsx-countries'), 
    path('api/manufacturers/xlsx/', ExportManufacturerDataXlsxView.as_view(), name='xlsx-manufacturers'),
    path('api/cars/xlsx/', ExportCarDataXlsxView.as_view(), name='xlsx-cars'),
    path('api/comments/xlsx/', ExportCommentsDataXlsxView.as_view(), name='xlsx-comments'),

    path('api/countries/csv/', ExportCountryDataCSVView.as_view(), name='csv-countries'),
    path('api/manufacturers/csv/', ExportManufaturerDataCSVView.as_view(), name='csv-manufacturers'), 
    path('api/cars/csv/', ExportCarDataCSVView.as_view(), name='csv-cars'),
    path('api/comments/csv/', ExportCommentDataCSVView.as_view(), name='csv-comments'),

    path('api/token/', obtain_auth_token)
]  