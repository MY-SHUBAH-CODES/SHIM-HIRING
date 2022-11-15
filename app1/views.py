from django.core.mail import send_mail
from django.conf import settings
from email import message
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dataclasses import field, fields
from django.shortcuts import render,redirect
from .forms import Myform
from.models import userdata
from django.contrib.auth.models import User
from app1.models import userdata



@csrf_exempt
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Myform(request.POST)
        a=fm.data.get(all)
        print(a)
        id = request.POST.get('id')       
        firstname = fm['first_name'].data
        lastname = fm['last_name'].data
        fathername = fm['father_name'].data
        aboutyou = fm['about_you'].data
        profile = request.POST.get('profile')
        print(profile)
        user_data = userdata(id,firstname,lastname,fathername,aboutyou,profile)
        user_data.save()
        return redirect('.')
        # return render(request, 'home.html', {"useform":Myform})
    else:
        all_data=userdata.objects.all()
        return render(request,'home.html', {"useform": Myform,"user":User,"data":all_data})

def search_records(request,id):
    if request.method=='get':
        pass






    #     print(fm)
    #     firstname = fm.get('first_name')
    #     lastname = fm.get('last_name')
    #     fathername = fm.get('father_name')
    #     aboutyou = fm.get('about_you')
    #     profile = fm.get('profile')
    #     user_data = userdata(id, firstname, lastname,fathername, aboutyou, profile)
    #     user_data.save()
    #     print(fm)
    #     return render(request, 'home.html', {"useform": fm})
    # else:
    #     fm = Myform()
    #     return render(request, 'home.html', {"useform": fm})


        

def about(request):
    # return render(self,'about.html')
    
    return render(request,'about.html')



def contact(self):
    return render(self, 'contact.html')

    