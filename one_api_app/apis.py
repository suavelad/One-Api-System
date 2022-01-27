from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from  drf_yasg import openapi
from  rest_framework.viewsets import ModelViewSet

from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from django.utils.decorators import  method_decorator
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *
import datetime ,requests,json,base64,coreapi

from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login, logout, get_user_model

from django.conf import settings
from decouple  import config


api_key = config('api_key')
request_header = {'Content-Type': 'application/json','Authorization': f'Bearer {api_key}'}
get_all_characters_url ='https://the-one-api.dev/v2/character'
get_all_movies_url ='https://the-one-api.dev/v2/movie'
get_all_quotes_url ='https://the-one-api.dev/v2/quote'
get_all_chapters_url ='https://the-one-api.dev/v2/chapter'


class GetAllCharactersView(APIView):
    
    # permission_classes= (AllowAny,) #For now, it is open
  
    
    def get(self, request):
        
        try:
            r = requests.get(get_all_characters_url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                      
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Characters pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
               
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
                  
class GetAllChaptersView(APIView):
    
    # permission_classes= (AllowAny,) #For now, it is open
  
    
    def get(self, request):
        
        try:
            r = requests.get(get_all_quotes_url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                      
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Quotes pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
               
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
            
class GetAllQuotesView(APIView):
    
    # permission_classes= (AllowAny,) #For now, it is open
  
    
    def get(self, request):
        
        try:
            r = requests.get(get_all_quotes_url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                      
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Chapters pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
               
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)


class GetAllMoviesView(APIView):
    
    # permission_classes= (AllowAny,) #For now, it is open
  
    
    def get(self, request):
        
        try:
            r = requests.get(get_all_movies_url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                      
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Movies pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
               
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
 
             

class GetQuotePerCharactersView(APIView):
        
    # permission_classes= (AllowAny,) #For now, it is open
  
    def get(self, request,id):
        
        try:
            url= f'{get_all_characters_url}/{id}/quote'
            r = requests.get(url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                        
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Data pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
            
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
            
  
      
class GetQuotePerMoviesView(APIView):
        
    # permission_classes= (AllowAny,) #For now, it is open
  
    def get(self, request,id):
        
        try:
            url= f'{get_all_movies_url}/{id}/quote'
            r = requests.get(url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                        
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':str(len(response['docs']))+ ' Data pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
            
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
            
        
         
class GetMoviePerIdView(APIView):
        
    # permission_classes= (AllowAny,) #For now, it is open
  
    def get(self, request,id):
        
        try:
            url= f'{get_all_movies_url}/{id}'
            r = requests.get(url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                        
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':' Data pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
            
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
            
class GetQuotePerIdView(APIView):
        
    # permission_classes= (AllowAny,) #For now, it is open
  
    def get(self, request,id):
        
        try:
            url= f'{get_all_quotes_url}/{id}'
            r = requests.get(url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                        
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':' Data pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
            
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
        

class GetChapterPerIdView(APIView):
        
    # permission_classes= (AllowAny,) #For now, it is open
  
    def get(self, request,id):
        
        try:
            url= f'{get_all_chapters_url}/{id}'
            r = requests.get(url,headers=request_header)
            response= r.json()
            
            paginator = LimitOffsetPagination()
            result_page = paginator.paginate_queryset(response['docs'], request) 
            result=paginator.get_paginated_response(result_page)
            output = result.data
            
                        
            if r.status_code == 200:
                return Response({'code':200,
                                'status':'success',
                                'message':' Data pulled successfully.',
                                'data':output
                                            },status=status.HTTP_200_OK)
            else:
                return Response({'code':400,
                    'status':'error',
                    'message':'An error occurred when calling the api '},status=status.HTTP_400_BAD_REQUEST)
        
            
        except :
            return Response({'code':400,
                'status':'error',
                'message':'An error occurred '},status=status.HTTP_400_BAD_REQUEST)
        
     
              
                
            
        






