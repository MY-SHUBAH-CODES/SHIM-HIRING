from django.contrib import admin
from .models import BASIC_DATA

# Register your models here.


class BASIC_DATAAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','father_name','mother_name','about_you','profile')
admin.site.register(BASIC_DATA,BASIC_DATAAdmin)
                    
                    
                    
                   



