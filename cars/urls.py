from django.urls import path
from .views import cars_view  

urlpatterns = [
    path('', cars_view, name='cars_view'),  
]
