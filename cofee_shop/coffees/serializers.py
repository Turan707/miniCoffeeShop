from rest_framework.serializers import ModelSerializer
from .models import Coffee


class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'
        
        
        
class CoffeePreviewSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = [
            'id',
            'name'
        ]
        