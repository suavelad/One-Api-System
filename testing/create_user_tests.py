import re

from .conftest import unexpected_response_error
from django.urls import reverse


get_all_characters_url = reverse('get-all-characters')
get_all_movies_url = reverse('get-all-movies')
get_all_chapters_url = reverse('get-all-chapters')
get_all_quotes_url = reverse('get-all-quotes')
create_user_url = reverse('create-member')
login_url = reverse('login')


def test_create_user(client, default_user):
    """Create raffle from whitelisted manager ip address"""

    resp = client.post(create_user_url, data=default_user)
    assert resp.status_code == 201, unexpected_response_error(resp)

def test_login(authenticate_user,client, default_login_user ):
    """Login"""  
    user = authenticate_user
    login_resp = client.post(login_url,data=default_login_user)
    
    assert login_resp.status_code == 200,unexpected_response_error(login_resp)
    assert 'access' in login_resp.data





