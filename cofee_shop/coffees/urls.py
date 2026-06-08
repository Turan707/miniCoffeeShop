from django.urls import path
from .views import greet_api

urlpatterns = [
    path(
        'api/v1/coffees', greet_api
    )
]
