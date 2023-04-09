def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404
    assert response.json == {'error': 'NotFound', 'message': '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}
