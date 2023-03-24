
from django.urls import path
from film.views import test_response

urlpatterns = [
    path('test/', test_response)
]
