from django.http import JsonResponse
from .models import Coffee

def greet_api(request):
    coffee_data = list(Coffee.objects.values())
    return JsonResponse(coffee_data, safe=False)