from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,),
    path('about', views.indexx,),
    path('t-join', views.indexxx,),
    path('vertical-weld', views.indexxxx,),
    path('join', views.indexxxxx,),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)