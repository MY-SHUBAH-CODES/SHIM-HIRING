from django.shortcuts import render


# Create your views here.
def home(self):
    return render(self,'home.html')

def about(self):
    return render(self,'about.html')
    