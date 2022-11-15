from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    
    path('',views.home,name="home"),
    path('search/<int:name/', views.search_records, name="search_records"),
    path(r'^about/$', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    
]
