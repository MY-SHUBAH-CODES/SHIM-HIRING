from django.core.mail import send_mail
from django.conf import settings
from email import message
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dataclasses import field, fields
from django.shortcuts import render,redirect
from .forms import Myform
# from.models import userdata
from django.contrib.auth.models import User
from app1.models import BASIC_DATA
from django.core.mail import send_mail




@csrf_exempt
# Create your views here.
def add_applicant(request):
    if request.method == 'POST':
        fm = Myform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('.')

        # a=fm.data.get(all)
        # # print(a)
        # id = request.POST.get('id')       
        # firstname = fm['first_name'].data
        # lastname = fm['last_name'].data
        # fathername = fm['father_name'].data
        # mothername =  fm['mother_name'].data
        # aboutyou = fm['about_you'].data
        # file=request.FILES
        # print(file)
        # profile = request..get('profile')
        # # print(profile)
        # user_data =BASIC_DATA(id,firstname,lastname,fathername,mothername,aboutyou,profile)
        # user_data.save()
        # return render(request, 'home.html', {"useform":Myform})
    else:
        return render(request,'add_applicant.html',{"useform": Myform})

        # all_data=BASIC_DATA.objects.all()

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


        

def about(request,pk):
    data=BASIC_DATA.objects.get(id=pk)
    print(data.profile.path)
    return render(request,'about.html',{"data":data})

    return render(request,'about.html')

def your_applicant(request):
    data=BASIC_DATA.objects.all()
    return render(request,'your_applicant.html',{'all_data':data})
    
    
   




def contact(self):
    return render(self, 'contact.html')

def send_email(request):
    if request.method=='POST':
        send_mail(
            'just testing',
            'did you got the this message.',
            'ethical900@gmail.com',
            ['shubhi231305@gmail.com'],
            fail_silently=False,
            )
        return HttpResponse("Email sent successfully\nteam will contact you shortly!",content_type='text/plain')

    
def home(request):
    return render(request,'home.html')