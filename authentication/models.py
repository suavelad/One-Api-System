from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager, PermissionsMixin)
from  .manager import CustomUserManager

# Create your models here.




class User (AbstractBaseUser, PermissionsMixin):


    id = models.AutoField(primary_key=True)
    email = models.EmailField( max_length=254, unique=True, db_index=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)   
    is_active= models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.email