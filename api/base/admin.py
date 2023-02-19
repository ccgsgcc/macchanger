from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
   list_display = ('slug', 'username', 'email', 'number', 'updated')
   
admin.site.register(Company, CompanyAdmin)
