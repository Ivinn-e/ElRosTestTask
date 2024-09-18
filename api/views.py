from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentsSerializer
from .models import Country, Manufacturer, Car, Comments
import io
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
import csv
from rest_framework import status 
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from rest_framework.generics import (CreateAPIView, RetrieveUpdateDestroyAPIView)   
from rest_framework.permissions import IsAuthenticated, AllowAny



# Endpoint для экспорта данных в формате xlsx или csv
class ExportXLSXandCSV(APIView):
    def get(self,  model_name, format):
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }

        if model_name not in models:
            return Response({"detail": "Invalid model."}, status=400)

        model = models[model_name]
        data = model.objects.all()

        fields = [field.name for field in model._meta.get_fields()]

        serialized_data = []
        for obj in data:
            obj_data = [getattr(obj, field) for field in fields]
            serialized_data.append(obj_data)

        if format == 'xlsx':
            df = pd.DataFrame(serialized_data, columns=fields)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={model_name.lower()}_export.xlsx'
            df.to_excel(response, engine='openpyxl', index=False)
            return response
        elif format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={model_name.lower()}_export.csv'
            writer = csv.writer(response)
            writer.writerow(fields)
            writer.writerows(serialized_data)
            return response
        

# Endpoint для просмотра записей модели
class GetModelsData(APIView):
    def get(self, request, model_name):
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }

        serializers = {
            Country: CountrySerializer,
            Car: CarSerializer,
            Manufacturer: ManufacturerSerializer,
           
            Comments:  CommentsSerializer
        }
        model = models[model_name]

        queryset = model.objects.all()
        serializer_class = serializers[model]

        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data) 
    

# Endpoint для создания записи модели
class CreateModelsData(CreateAPIView):
    def get_serializer_class(self):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        model_name = self.kwargs.get('model_name')
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }
        serializers = {
            Country: CountrySerializer,
            Car: CarSerializer,
            Manufacturer: ManufacturerSerializer,
            Comments: CommentsSerializer
        }
        model = models.get(model_name)
        return serializers.get(model)
    
    def get_permissions(self):
        model_name = self.kwargs.get('model_name')
        if model_name == 'Comments':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
        
    def get(self, request, model_name):
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Endpoint для просмотра, обновления и удаления записи модели 
class RetrieveUpdateDestroyData(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        model_name = self.kwargs.get('model_name')
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }
        serializers = {
            Country: CountrySerializer,
            Car: CarSerializer,
            Manufacturer: ManufacturerSerializer,
            Comments: CommentsSerializer
        }
        model = models.get(model_name)
        return serializers.get(model)

    def get_queryset(self):
        model_name = self.kwargs.get('model_name')
        models = {
            'Country': Country,
            'Car': Car,
            'Manufacturer': Manufacturer,
            'Comments': Comments
        }
        model = models.get(model_name)
        return model.objects.all()