from django.urls import path
from .views import CoffeAPIView

urlpatterns = [
    path(
        'api/v1/coffees', CoffeAPIView.as_view()
    )
]
