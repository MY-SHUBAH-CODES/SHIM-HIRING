from django.urls import path, include
from app1 import views


urlpatterns = [
    path('home/',views.home,name="home"),
    


]
