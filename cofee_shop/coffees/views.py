from rest_framework.views import APIView, Response, status
from .models import Coffee
from .serializers import CoffeeSerializer, CoffeePreviewSerializer

class CoffeeAPIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee2APIView(APIView):
    def get(self, request):
        coffe_list = Coffee.objects.order_by('price')
        serializer = CoffeeSerializer(coffe_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee1APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.filter(is_available=True)
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee2APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.filter(price__gt=5)
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Coffee3APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.filter(rating__gt=4)
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee4APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.order_by('price')
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee5APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.order_by('-price')
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class Coffee6APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.order_by('-rating')
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Coffee7APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.filter(is_available=True, rating__gt=4)
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Coffee8APIView(APIView):
    def get(self, reauest):
        coffee_list = Coffee.objects.order_by('-price')[:3]
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Cofee9APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.order_by('name')
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Coffee10APIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.filter(price__lt=10)
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)