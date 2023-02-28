from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
   list_display = ('slug', 'name', 'email', 'number', 'updated', 'created')
   prepopulated_fields = {'slug': ('name',)}
   
admin.site.register(Company, CompanyAdmin)