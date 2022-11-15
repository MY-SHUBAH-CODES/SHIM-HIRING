from django.contrib import admin
from .models import userdata

# Register your models here.


class UserdataAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','father_name','about_you','profile')
admin.site.register(userdata,UserdataAdmin)
                    
                    
                    
                   



