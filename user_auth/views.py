from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
csrf_exempt

def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'auth/signup.html', {"form":UserCreationForm})

    return render(request, 'auth/signup.html', {"form":UserCreationForm})

@csrf_exempt
def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return render(request,'home.html')
    else:
        return render(request,'auth/signin.html')


def signout(request):
    logout(request)
    return render(request,'home.html')
       

def reset_pass(request):
    pass


