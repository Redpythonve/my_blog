from django.urls import path # type: ignore
from . import views

urlpatterns = [
   
    path('create/', views.create, name='create'),
]