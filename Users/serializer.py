from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[field.name for field in User._meta.get_fields() if field.name is not 'password']
        # fields='__all__'