from django.urls import path
from . import views

urlpatterns = [
   path('', views.usersView, name='users'),
   path('<str:slug>', views.userView, name='user'),
]