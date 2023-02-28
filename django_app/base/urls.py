from  django.urls import path
from . import views

urlpatterns = [
   path("company/<str:slug>/", views.showCompany, name="company")
]