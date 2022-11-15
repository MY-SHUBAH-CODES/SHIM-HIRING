from django.shortcuts import render


# Create your views here.


def signup(request):
    return render(request,'auth/signup.html')
   


def login(request):
    pass

def reset_pass(request):
    pass


