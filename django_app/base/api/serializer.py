from rest_framework.serializers import ModelSerializer
from ..models import Company


class UserSerializer(ModelSerializer):
   class Meta:
      model = Company
      fields = '__all__'
      
   def to_representation(self, instance):
      return super().to_representation(instance)   
      data = {
         'slug': "slug"
      }
      return data
   
   def to_internal_value(self, data):
      data = {
         'slug': "slug"
      }
      return super().to_internal_value(data)