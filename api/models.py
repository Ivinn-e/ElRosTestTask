from django.core.validators import MinLengthValidator
from django.db import models    

class Country(models.Model):
    name = models.CharField('Страна', max_length=25)

class Manufacturer(models.Model):
    name = models.CharField('Производитель', max_length=60)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='manufacturers')


class Car(models.Model):
    name = models.CharField('Автомобиль', max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    yearOnRelease = models.IntegerField('Год начала выпуска')
    yearOfGraduation = models.IntegerField('Год окончания выпуска')

class Comments(models.Model):
    car = models.ForeignKey( Car, on_delete=models.CASCADE, related_name='comments')
    manufacturer = models.ForeignKey( Manufacturer, on_delete=models.CASCADE, related_name='comments')
    email = models.CharField('Email', max_length=100, validators=[MinLengthValidator(9)])
    dateOfCreation = models.DateTimeField('Дата создания', auto_now_add=True)   
    comment = models.CharField('Комментарий', max_length=10000, validators=[MinLengthValidator(5)])

    
