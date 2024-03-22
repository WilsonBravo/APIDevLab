from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class customFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = customFields
        fields = ['birthdate','gender']

class UserSerializer(serializers.ModelSerializer):
    custom_fields = customFieldsSerializer()
    class Meta:
        model=User
        # fields=[field.name for field in User._meta.get_fields() if field.name is not 'password']
        # fields='__all__'
        fields = ['id', 'username','first_name','last_name', 'email','password','custom_fields']

class loginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # fields=[field.name for field in User._meta.get_fields() if field.name is not 'password']
        # fields='__all__'
        fields = ['id', 'username','first_name','last_name', 'email']

class profileSerializer(serializers.ModelSerializer):
    custom_fields = customFieldsSerializer(source='customfields')
    class Meta:
        model=User
        fields=['id', 'is_staff', 'username','first_name','last_name', 'groups', 'date_joined', 'last_login', 'custom_fields']

    def to_representation(self, instance):
        if not instance.is_staff:
            return super().to_representation(instance)
        else:
            return None