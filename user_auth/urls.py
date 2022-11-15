from django.urls import path, include
from user_auth import views

urlpatterns = [


    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="about"),
    path('reset_pass/', views.reset_pass, name="reset_pass"),

]
