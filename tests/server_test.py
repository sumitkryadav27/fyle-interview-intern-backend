def test_invalid_route(client):
    response = client.get('/invalid')
    error_response = response.json
    
    assert response.status_code == 404
    assert error_response['error'] == 'NotFound'
    assert error_response["message"] == '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'
