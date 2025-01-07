from django.urls import path # type: ignore
from . import views

urlpatterns = [
   
    path('restaurant/', views.restaurant, name='restaurant'),
]