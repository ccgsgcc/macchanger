from django.db import models
from django.utils.text import slugify

class Company(models.Model):
   name = models.CharField(max_length=50)
   slug = models.CharField(max_length=100, unique=True, default='')
   
   # DATA ABOUT COMPANY
   title = models.CharField(max_length=50, blank=True)
   number = models.CharField(max_length=20, blank=True)
   email = models.EmailField(max_length=100, blank=True)
   ava = models.ImageField(upload_to='avatars', blank=True)
   location = models.CharField(max_length=164, blank=True)
   about = models.TextField(max_length=500, blank=True)
   
   #SOCIAL MEDIA
   facebook = models.CharField(max_length=1000, blank=True)
   instagram = models.CharField(max_length=1000, blank=True)
   youtube = models.CharField(max_length=1000, blank=True)
   telegram = models.CharField(max_length=1000, blank=True)
   twitter = models.CharField(max_length=1000, blank=True)
   tiktok = models.CharField(max_length=1000, blank=True)
   pinterest = models.CharField(max_length=1000, blank=True)
   snapChat = models.CharField(max_length=1000, blank=True)
   linkedin = models.CharField(max_length=1000, blank=True)
   tumbler = models.CharField(max_length=1000, blank=True)
   vk = models.CharField(max_length=1000, blank=True)
   discord = models.CharField(max_length=1000, blank=True)
   twitch = models.CharField(max_length=1000, blank=True)
   quora = models.CharField(max_length=1000, blank=True)
   whatsapp = models.CharField(max_length=1000, blank=True)
   github = models.CharField(max_length=1000, blank=True)
   sinaweibo = models.CharField(max_length=1000, blank=True)
   viber = models.CharField(max_length=1000, blank=True)
   skype = models.CharField(max_length=1000, blank=True)
   
   soundCloud = models.CharField(max_length=1000, blank=True)
   spotify = models.CharField(max_length=1000, blank=True)
   
   their_website1 = models.CharField(max_length=1000, blank=True)
   their_website2 = models.CharField(max_length=1000, blank=True)
   their_website3 = models.CharField(max_length=1000, blank=True)
   
   yandex_taxi = models.CharField(max_length=1000, blank=True)
   yandex_cards = models.CharField(max_length=1000, blank=True)
   google_cards = models.CharField(max_length=1000, blank=True)
   
   #STYLE
   background_color = models.CharField(max_length=10, default="#202020")
   color = models.CharField(max_length=10, default="#ffffff")
   
   #Card
   card_background_color = models.CharField(max_length=20, default="transparent")
   card_border_radius = models.CharField(max_length=40, default="10px")
   card_box_shadow = models.CharField(max_length=100, default="1px 1px  20px 5px rgb(20,20,20, .4)")
   card_border   = models.CharField(max_length=40, default="1px solid rgb(20,20,20, .4)")
   
   #Image
   card_image_border_radius = models.CharField(max_length=40, default="1000px")
   card_image_width = models.CharField(max_length=10, default="100px")
   card_image_height = models.CharField(max_length=10, default="100px")
   
   #TITLE
   card_title_font_size = models.CharField(max_length=40, default="20px")
   card_title_font_family = models.CharField(max_length=40, blank=True, default="")
   card_title_font_color = models.CharField(max_length=40, blank=True, default="")
   card_title_font_weight = models.CharField(max_length=10, default='bold')
   
   #Text 
   card_text_font_size = models.CharField(max_length=10, default='18px')
   card_text_font_family = models.CharField(max_length=30, blank=True, default="")
   card_text_color = models.CharField(max_length=20, blank=True)
   card_text_font_weight = models.CharField(max_length=10, blank=True, default="")
   card_text_box_shadow = models.CharField(max_length=30, default='', blank=True)
   card_text_border_bottom = models.CharField(max_length=20, default='', blank=True)
   card_text_border = models.CharField(max_length=20, default='', blank=True)
   
   #Label Text 
   card_label_font_size = models.CharField(max_length=10, default='14px')
   card_label_font_family = models.CharField(max_length=30, blank=True)
   card_label_color = models.CharField(max_length=20, blank=True)
   card_label_font_weight = models.CharField(max_length=5, default="400")

   #Line Text 
   card_line_background_color = models.CharField(max_length=20, blank=True, default='white')
   card_line_height = models.CharField(max_length=10, default='2px');
   card_line_background = models.CharField(max_length=100, blank=True, default='')
   card_line_border_radius = models.CharField(max_length=100, default="10px", blank=True)
   
   # Add Contact Button
   card_button_background_color = models.CharField(max_length=20, default="white")
   card_button_color = models.CharField(max_length = 20, default="black")
   card_button_border_radius = models.CharField(max_length=20, default='10px')
   card_button_box_shadow = models.CharField(max_length=40, default='none')
   
   # Add Contact Button hover
   card_button_background_color_hover = models.CharField(max_length=20, default="black")
   card_button_color_hover = models.CharField(max_length = 20, default="white")
   card_button_border_radius_hover = models.CharField(max_length=20, blank=True, default="")
   card_button_box_shadow_hover = models.CharField(max_length=40, default='none')
   
   #Icon
   card_icon_color = models.CharField(max_length=20, blank=True)
   font_icon_size = models.CharField(max_length=20, default="36px")
   
   #Icon Hover
   card_icon_color_hover = models.CharField(max_length=20, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name)
      super(Company, self).save(*args, **kwargs)
      
   def __str__(self):
      return self.name