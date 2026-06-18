from rest_framework.views import APIView, Response, status
from .models import Coffee
from .serializers import CoffeeSerializer, CoffeePreviewSerializer

class CoffeAPIView(APIView):
    def get(self, request):
        coffee_list = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee_list, many=True)
        
        print(coffee_list)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)