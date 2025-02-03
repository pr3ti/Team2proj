import pytest
from carapp import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test home page loads correctly
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Car Inventory" in response.data  # Check if the page title is in the response

# Test adding a new car via form
def test_add_car(client):
    response = client.post('/add', data={'make': 'Nissan', 'model': 'Altima', 'year': '2023'})
    assert response.status_code == 302  # Redirect after adding
    home_response = client.get('/')
    assert b"Nissan" in home_response.data  # Check if car appears on the page

# Test updating a car
def test_update_car(client):
    response = client.post('/update/2', data={'make': 'Mazda', 'model': 'CX-5', 'year': '2022'})
    assert response.status_code == 302  # Redirect after updating
    home_response = client.get('/')
    assert b"Mazda" in home_response.data  # Check if updated car appears

# Test deleting a car
def test_delete_car(client):
    response = client.get('/delete/2')
    assert response.status_code == 302  # Redirect after deleting
