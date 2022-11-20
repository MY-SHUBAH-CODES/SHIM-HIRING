from django.db import models

class BASIC_DATA(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length= 200)
    mother_name=models.CharField(max_length=200, default='')
    about_you = models.TextField()
    profile = models.ImageField(upload_to="media/profile_images")
