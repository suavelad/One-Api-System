import ipaddress
import os

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from authentication.models import User
from django_dynamic_fixture import G


get_all_characters_url = reverse('get-all-characters')
get_all_movies_url = reverse('get-all-movies')
get_all_chapters_url = reverse('get-all-chapters')
get_all_quotes_url = reverse('get-all-quotes')
create_user_url = reverse('create-member')
login_url = reverse('login')

DEFAULT_USER= {
    "name":"Doe Jack",
    "email": "sunnexajayi@gmail.com",
    "password": 'password@123',
    "username":"djack"
    
}

DEFAULT_LOGIN_USER= {
    "email": "sunnexajayi@gmail.com",
    "password": 'password@123'
    
}


class OneAPIClient(APIClient):
    default_format = 'json'


def unexpected_response_error(resp):
    return f'Unexpected response {resp.status_code} / {resp.content}'


@pytest.fixture
def client():
    return OneAPIClient()


@pytest.fixture(autouse=True)
def autouse_db(db):
    pass

@pytest.fixture
def default_user():
    return DEFAULT_USER



@pytest.fixture
def default_login_user():
    return DEFAULT_LOGIN_USER


@pytest.fixture
def authenticate_user(client):
    ''' Create a new user '''
    user = G(User,email='sunnexajayi@gmail.com')
    user.set_password('password@123')
    user.save()
    
    '''Login the user '''
    user=client.login(email='sunnexajayi@gmail.com',password='password@123')
    return user
    
# @pytest.fixture
# def authenticate_user(client):
#     ''' Create a new user '''
#     user = G(User,email='sunny@test.com')
#     user.set_password('password@123')
#     user.save()
    
#     '''Login the user '''
#     user_login=client.post(login_url,data=default_login_user)
#     return user_login





