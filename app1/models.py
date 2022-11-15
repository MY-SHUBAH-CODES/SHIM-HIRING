from django.db import models

class userdata(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length= 200)
    about_you = models.TextField()
    profile = models.ImageField(upload_to="profile_images")
