
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from  drf_yasg import openapi
from  rest_framework.viewsets import ModelViewSet,GenericViewSet

from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from django.utils.decorators import  method_decorator
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, UserRegistrationSerializer, LoginSerializer
from .models import User
import datetime ,requests,json
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login, logout, get_user_model

from django.conf import settings

# from .token import default_token_generator
# from .utils import get_random_string, generateKey
import base64,coreapi

from django.core.mail import send_mail
from rest_framework import mixins




class CreateUserView(APIView):
    permission_classes= (AllowAny,) 


    @swagger_auto_schema(request_body=UserRegistrationSerializer) 
    def post(self, request,*args,**kwargs):

        
        # serializer = self.get_serializer(data=request.data)
        # try:
        
        serializer = UserRegistrationSerializer(data=request.data)

        
        if  serializer.is_valid(): 
            result=serializer.save()
            email=result['email']
            
            user = User.objects.get(email=email) 
            refresh = RefreshToken.for_user(user)
            
            #Send otp to user 
            try:
                user = User.objects.get(email=email, is_active=True)
                
                return Response({'code':201,
                        'status':'success',
                        'message':'User created successfully',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'access_duration': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
                        },status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                    return Response({'message':'User with the email does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        else:
            default_errors = serializer.errors
            print(default_errors)
            error_message = ''
            for field_name, field_errors in default_errors.items():
                error_message += f'{field_name} is {field_errors[0].code},'
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'code': 400,
                'status':'error',
                'message': error_message
                }, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class LoginView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]
    
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self,request):
        
        serializer= LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                user= User.objects.get(email=email)
                refresh = RefreshToken.for_user(user)
            except:
                return Response({'code':401,
                                'status':'error',
                                'message':'User does not exist'},status=status.HTTP_401_UNAUTHORIZED)
                
            
           
            if user.is_active:
                    if user.check_password(password):
     
                        the_serializer= UserSerializer 
                        user_data = the_serializer(user).data
                    
                        return Response({
                            'code':200,
                            'status':'success',
                            'message':'Login Sucessful',
                            'user_info':user_data,
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'access_duration': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
                        },status=status.HTTP_200_OK)
                            
                    else:
                        return Response({'code':401,
                            'status':'error',
                            'message':'Incorrect Password Inserted'},status=status.HTTP_401_UNAUTHORIZED)
                
            else:
                return Response({'code':401,
                    'status':'error',
                    'message':'User is not active. Kindly contact your admin'},status=status.HTTP_401_UNAUTHORIZED)
                        
            
class UserViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,GenericViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

        