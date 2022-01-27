
import datetime
from django.conf import settings
from rest_framework import serializers
from .models import *
from rest_framework.generics import get_object_or_404
from django.core.mail import  send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password


class ConfirmResetTokenSerializer (serializers.Serializer):
    otp_code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)






