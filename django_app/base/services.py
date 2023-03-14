from .models import *

def get_product(slug):
   return  Company.objects.get(slug = slug)

def get_all_products(slug):
   return Company.objects.all()
   