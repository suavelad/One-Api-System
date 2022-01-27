import datetime
from django.conf import settings
from rest_framework import serializers
from .models import User
from rest_framework.generics import get_object_or_404
from django.core.mail import  send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        exclude = ('is_active','password','is_superuser','user_permissions','groups' )
 


    
class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    username= serializers.CharField(required=False)
    
    
    class Meta:
        model = User
        fields = ('__all__')
        
        
    
    def create(self,validated_data):
       
        password = validated_data.pop('password')
        username = validated_data['username']
        email = validated_data['email'] 

        
        try:
            existing_user = User.objects.get(email=email)   
        except:
            existing_user = ''
            
        if not existing_user:
     
            try:
                mem_user = User.objects.create(email=email,username=username)
                mem_user.set_password(password)
                mem_user.is_active=True 
                mem_user.save()

                                    
            except :
                raise serializers.ValidationError({'code': 400,
                                                    'status':'error',
                                                    'message': 'Error occurred when creating this user'})
                    

                
        else:
            raise serializers.ValidationError({'code': 400,
                                                'status':'error',
                                                'message': 'User already exist'})
       
            
        return validated_data


class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
