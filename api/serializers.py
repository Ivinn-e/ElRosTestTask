from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comments

class CountrySerializer(serializers.ModelSerializer):
        manufacturers = serializers.SerializerMethodField()

        class Meta:
                model = Country
                fields = ('id', 'name', 'manufacturers')

        def get_manufacturers(self, obj):
                manufacturer_data = ManufacturerSerializer(obj.manufacturers.all(), many=True).data
                return [manufacturer['name'] for manufacturer in manufacturer_data]        
                

class ManufacturerSerializer(serializers.ModelSerializer):
        cars = serializers.SerializerMethodField()

        class Meta:
                model = Manufacturer
                fields = ('id', 'name', 'country', 'cars')

        def get_cars(self, obj):
                cars = obj.cars.all()
                return [{
                'name': car.name,
                'comment_count': car.comments.count()
                }               
                for car in cars]



class CarSerializer(serializers.ModelSerializer):
        comment_count = serializers.SerializerMethodField()

        class Meta:
                model = Car
                fields = ('id', 'name', 'manufacturer', 'yearOnRelease', 'yearOfGraduation', 'comment_count')
        
        def get_comment_count(self, obj):
                return obj.comments.count()


class CommentsSerializer(serializers.ModelSerializer):
        manufacturer = serializers.PrimaryKeyRelatedField(read_only=True)

        class Meta:
                model = Comments
                fields = ('id', 'email', 'car', 'comment', 'manufacturer')

        def create(self, validated_data):
                car = validated_data.get('car')
                validated_data['manufacturer'] = car.manufacturer
                return super().create(validated_data)
        
