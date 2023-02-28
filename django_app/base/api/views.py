from ..models import Company
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .utils import slugGenerate, requestCheck
from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET'])
def usersView(request):
   # ! CREATE NEW USER
   if request.method == 'POST':
      name = request.POST.get('name')      
      photo = ""
      
      if 'ava' in request.FILES:
         photo = request.FILES['ava']
      else: 
         photo = ''         
         
      form  = Company.objects.create(
         slug = slugGenerate(name),
         name = name,
         
         title = requestCheck(request.POST.get('title')),
         number = requestCheck(request.POST.get('number')),
         email = requestCheck(request.POST.get('email')),
         ava = photo,
         location = requestCheck(request.POST.get('location')),
         
         facebook = requestCheck(request.POST.get('facebook')),
         instagram = requestCheck(request.POST.get('instagram')),
         youtube = requestCheck(request.POST.get('youtube')),
         telegram = requestCheck(request.POST.get('telegram')),
         twitter = requestCheck(request.POST.get('twitter')),
         tiktok = requestCheck(request.POST.get('tiktok')),
         pinterest = requestCheck(request.POST.get('pinterest')),
         
         vk = requestCheck(request.POST.get('vk')),
         linkedin = requestCheck(request.POST.get('linkedin')),
         tumbler = requestCheck(request.POST.get('tumbler')),
         discord = requestCheck(request.POST.get('discord')),
         twitch = requestCheck(request.POST.get('twitch')),
         quora = requestCheck(request.POST.get('quora')),
         whatsapp = requestCheck(request.POST.get('whatsapp')),
         github = requestCheck(request.POST.get('github')),
         sinaweibo = requestCheck(request.POST.get('sinaweibo')),
         viber = requestCheck(request.POST.get('viber')),
         skype = requestCheck(request.POST.get('skype')),
         
         soundCloud = requestCheck(request.POST.get('soundCloud')),
         spotify = requestCheck(request.POST.get('spotify')),
         
         their_website1 = requestCheck(request.POST.get('their_website1')),
         their_website2 = requestCheck(request.POST.get('their_website2')),
         their_website3 = requestCheck(request.POST.get('their_website3')),
      )
      
      form.save()
      return Response({
         "message": "has been created successfully",
         
      }, status=200)
         
   # ! ENTER ALL USERS 
   if request.method == 'GET':
      objects = Company.objects.all()
      
      if (object):
         return Response(UserSerializer(objects, many=True).data, status=200)
      else: 
         return Response({"message": "USers not found"}, status=200)
      
      
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def userView(request, slug):
   user = get_object_or_404(Company, slug=slug)
   
   if user:
      #! GET ONE USER
      if request.method == 'GET':
         # return Response(UserSerializer(user, many=False).data, status=200)
         return Response({
            'slug': user.slug,
            'username': user.name,
            'title': user.title,
            'number': user.number,
            'email': user.email,
            'ava': str(user.ava),
            'location': user.location,
            'social_medias': {
               'facebook': user.facebook,
               'instagram': user.instagram,
               'youtube': user.youtube,
               'telegram': user.telegram,
               'twitter': user.twitter,
               'tiktok': user.tiktok,
               'pinterest': user.pinterest,
               'snapChat': user.snapChat,
               'linkedin': user.linkedin,
               'tumbler': user.tumbler,
               'vk': user.vk,
               'discord': user.discord,
               'twitch': user.twitch,
               'quora': user.quora,
               'whatsapp': user.whatsapp,
               'github': user.github,
               'sinaweibo': user.sinaweibo,
               'viber': user.viber,
               'skype': user.skype,
               'soundCloud': user.soundCloud,
               'spotify': user.spotify,
               
               'their_website1': user.their_website1,
               'their_website2': user.their_website2,
               'their_website3': user.their_website3,
            }
         })
      
      #! UPDATE USER
      if request.method == 'PUT' or 'PATCH':
         image = ''
         
         if 'ava' in request.FILES: 
            image = request.FILES
         else:
            image = ''
         
         serializer = UserSerializer(user, data=request.data, files=image)
         
         if  serializer.is_valid():
            serializer.save()
            return Response(
               {
                  'message': "Has been updated successfully",
                  'data': serializer.data
               }, 
               status=200
            )
         else:
            return Response(serializer.errors, status=400)
         
      # ! DELETE USER
      if request.method == 'DELETE': 
         user.delete()
         
         return Response({'message': "Delete was successful"}, status=200)
   return Response({"message": "User not found"}, status=404)