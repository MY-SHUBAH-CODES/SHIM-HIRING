from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    
    path('',views.home,name="home"),
    path('add_applicant/', views.add_applicant, name="add_applicant"),
    path('your_applicant/', views.your_applicant, name="your_applicant"),
    path('about/<int:pk>/', views.about, name="about"),
    path('send_email/', views.send_email, name="send_email"),
    path('contact/', views.contact, name="contact"),

    
]
