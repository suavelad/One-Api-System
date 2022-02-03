
import re

from .conftest import unexpected_response_error
from django.urls import reverse

get_all_characters_url = reverse('get-all-characters')
get_all_movies_url = reverse('get-all-movies')
get_all_chapters_url = reverse('get-all-chapters')
get_all_quotes_url = reverse('get-all-quotes')
create_user_url = reverse('create-member')
login_url = reverse('login')




def test_get_all_characters_unauthenticated(client ):
    """Not authenticated"""

    resp = client.get(get_all_characters_url)
    
    assert resp.status_code == 401, unexpected_response_error(resp)


def test_get_all_characters_authenticated(authenticate_user,client, default_login_user ):
    """All Characters"""
    
    user = authenticate_user
    login_resp = client.post(login_url,data=default_login_user)
    
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_resp.data['access'])
    # resp = client.get(get_all_characters_url,headers={'Content-Type': 'application/json','Authorization': 'Bearer {}'.format(login_resp.data['access'])})
    resp = client.get(get_all_characters_url)
    assert resp.status_code == 200, unexpected_response_error(resp)


