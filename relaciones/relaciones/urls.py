
from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one/', include('one_one.urls')),
    path('manyone/', include('many_one.urls')),
    path('manymany/', include('many_many.urls')),
    
]
