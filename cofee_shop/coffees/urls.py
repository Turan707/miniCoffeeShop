from django.urls import path
from .views import(
    CoffeeAPIView, 
    Coffee2APIView, 
    Coffee1APIView,
    Coffee2APIView,
    Coffee3APIView,
    Coffee4APIView,
    Coffee5APIView,
    Coffee6APIView,
    Coffee7APIView,
    Coffee8APIView,
    Cofee9APIView,
    Coffee10APIView
    
    ) 

urlpatterns = [
    path(
        'api/v1/coffees/', CoffeeAPIView.as_view()
    ), 
    path(
        'api/v1/coffees_2/', Coffee2APIView.as_view()
    ), 
    path(
        'api/v1/coffee1/', Coffee1APIView.as_view()
    ),
    path(
        'api/v1/coffee2/', Coffee2APIView.as_view()
    ),
    path(
        'api/v1/coffee3/', Coffee3APIView.as_view()
    ),
    path(
        'api/v1/coffee4/', Coffee4APIView.as_view()
    ),
    path(
        'api/v1/coffee5/', Coffee5APIView.as_view()
    ),
    path(
        'api/v1/coffee6/', Coffee6APIView.as_view()
    ),
    path(
        'api/v1/coffee7/', Coffee7APIView.as_view()
    ),
    path(
        'api/v1/coffee8/', Coffee8APIView.as_view()
    ),
    path(
        'api/v1/coffee9/', Cofee9APIView.as_view()
    ),
    path(
        'api/v1/coffee10/', Coffee10APIView.as_view()
    )
]
