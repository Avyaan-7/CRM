from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'), #route,url,function_name
]