from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('t-join', include('main.urls')),
    path('vertical-weld', include('main.urls')),
    path('join', include('main.urls')),
]
