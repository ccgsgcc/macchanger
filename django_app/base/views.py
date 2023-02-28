from django.shortcuts import render
from .models import Company

def showCompany(request, slug): 
   company = Company.objects.get(slug = slug)
   
   return render(request, 'main.html', {'company': company})
      