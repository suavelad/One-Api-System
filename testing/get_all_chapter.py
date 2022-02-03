def test_get_all_chapters_authenticated(authenticate_user,client, default_login_user ):
    """Test All Quotes"""
    
    user = authenticate_user
    login_resp = client.post(login_url,data=default_login_user)
    
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_resp.data['access'])
    # resp = client.get(get_all_characters_url,headers={'Content-Type': 'application/json','Authorization': 'Bearer {}'.format(login_resp.data['access'])})
    resp = client.get(get_all_chapters_url)
    assert resp.status_code == 200, unexpected_response_error(resp)


