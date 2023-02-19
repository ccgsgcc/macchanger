from django.db import models

class Company(models.Model):
   slug = models.CharField(max_length=100, unique=True, default='')
   username = models.CharField(max_length=50)
   
   title = models.CharField(max_length=50, blank=True)
   number = models.CharField(max_length=20, blank=True)
   email = models.EmailField(max_length=100, blank=True)
   ava = models.ImageField(upload_to='avatars', blank=True)
   location = models.CharField(max_length=164, blank=True)
   
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
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.username