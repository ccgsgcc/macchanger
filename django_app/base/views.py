from django.shortcuts import render, redirect
from base.api.utils import slugGenerate
from .models import Company
from .utils import slugGenerate
from .services import get_product, get_all_products   

def showCompany(request, slug: str): 
   company = get_product(slug)
   return render(request, 'index.html', {'company': company})

def home(request):
   # if request.user.is_authenticated:
      companies = get_all_products()
      
      context = {'companies': companies}
      return render(request, 'admin/home.html', context)
   # else: 
   #    return redirect('/admin')
   
def create(request):
   # if request.user.is_authenticated:
      if request.method == 'POST':
         name = request.POST.get('name')
         title = request.POST.get('title')
         number = request.POST.get('number')
         email = request.POST.get('email')
         location = request.POST.get('location')
         about = request.POST.get('about')
         ava = request.FILES.get('ava')
         slug = slugGenerate(name)
         
         form = Company.objects.create(
            name = name, 
            slug = slug,
            title = title, 
            number = number,
            email = email,
            location = location,
            about = about,
            ava = ava,
         )
         
         form.save()
         return redirect('base:constructor', slug)
      
      return render(request, 'admin/create.html')
   # else: 
   #    return redirect('/admin')

def constructor(request, slug:str):
   # if request.user.is_authenticated:
      company = get_product(slug)
      
      if request.method == 'POST':
         background_color = request.POST.get('background_color')
         
         company.background_color = background_color
         company.color = request.POST.get('color')
         
         company.card_background_color = request.POST.get('card_background_color')
         company.card_border_radius = request.POST.get('card_border_radius')
         company.card_box_shadow = request.POST.get('card_box_shadow')
         company.card_border = request.POST.get('card_border')
         
         company.card_image_border_radius = request.POST.get('card_image_border_radius')
         company.card_image_width = request.POST.get('card_image_width')
         company.card_image_height = request.POST.get('card_image_height')
         
         company.card_title_font_size = request.POST.get('card_title_font_size')
         company.card_title_font_family = request.POST.get('card_title_font_family')
         if  request.POST.get('card_title_font_color'):
            company.card_title_font_color = request.POST.get('card_title_font_color')
         company.card_title_font_weight = request.POST.get('card_title_font_weight')
         
         company.card_button_background_color = request.POST.get('card_button_background_color')
         company.card_button_color = request.POST.get('card_button_color')
         company.card_button_border_radius = request.POST.get('card_button_border_radius')
         company.card_button_box_shadow = request.POST.get('card_button_box_shadow')
         
         company.card_button_background_color_hover = request.POST.get('card_button_background_color_hover')
         company.card_button_color_hover = request.POST.get('card_button_color_hover')
         company.card_button_border_radius_hover = request.POST.get('card_button_border_radius_hover')
         company.card_button_box_shadow_hover = request.POST.get('card_button_box_shadow_hover')
         
         if (request.POST.get('card_text_font_size')):
            company.card_text_font_size = request.POST.get('card_text_font_size')
         if request.POST.get('card_text_font_family'):
            company.card_text_font_family = request.POST.get('card_text_font_family')
         if request.POST.get('card_text_color'):
            company.card_text_color = request.POST.get('card_text_color')
         if request.POST.get('card_text_font_weight'):
            company.card_text_font_weight = request.POST.get('card_text_font_weight')
         if request.POST.get('card_text_box_shadow'):
            company.card_text_box_shadow = request.POST.get('card_text_box_shadow')
         if request.POST.get('card_text_border_bottom'):
            company.card_text_border_bottom = request.POST.get('card_text_border_bottom')
         if request.POST.get('card_text_border'):
            company.card_text_border = request.POST.get('card_text_border')
            
         card_label_font_size = request.POST.get('card_label_font_size')
         card_label_font_family = request.POST.get('card_label_font_family')
         card_label_color = request.POST.get('card_label_color')
         card_label_font_weight = request.POST.get('card_label_font_weight')
         
         if card_label_font_size:
            company.card_label_font_size = card_label_font_size
            
         if card_label_font_family:
            company.card_label_font_family = card_label_font_family
            
         if card_label_color:
            company.card_label_color = card_label_color
         
         if card_label_font_weight:
            company.card_label_font_weight = card_label_font_weight
            
         name = request.POST.get('name')
         if name:
            company.name = name
            
         ava = request.FILES.get('ava', None)
         if ava:
            company.ava = ava
            
         title = request.POST.get('title')
         if (company.title != title): company.title = title
         
         location = request.POST.get('location')
         if (company.location != location): company.location = location
         
         number = request.POST.get('number')
         if (company.number != number): company.number = number
         
         email = request.POST.get('email')
         if (company.email != email): company.email = email
         
         about = request.POST.get('about')
         if (company.about != about): company.about = about
         
         company.save()
      
      return render(request, 'admin/constructor.html', {'company': company})
   # else: 
   #    return redirect('/admin')
   
def cardDelete(request, slug:str):
   # if request.user.is_authenticated:
      company = get_product(slug)
      
      if company:
         if request.method == 'POST':
            company.delete()
            return redirect('base:home')
      
      return render(request, 'admin/delete.html', {'company': company})
   # else: 
   #    return redirect('/admin')  