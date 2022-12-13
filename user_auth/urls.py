from django.urls import path, include
from user_auth import views

urlpatterns = [


    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('reset_pass/', views.reset_pass, name="reset_pass"),

]
