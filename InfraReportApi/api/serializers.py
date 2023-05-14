from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):#Class to serialize
    class Meta:
        model = Product#Define the class(table)
        fields = '__all__'#Define the colums that will be serialized