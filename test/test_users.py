import pytest
from rest_framework.test import APIClient
from users.models import User
pytestmark = pytest.mark.django_db
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(): #we are making this user by sending this data directly to user model
    def make_user(**kwargs):
        return User.objects.create_user(
            email=kwargs.get('email', 'test@example.com'),
            username=kwargs.get('username', 'testuser'),
            password=kwargs.get('password', 'Testpass123!'),
            role=kwargs.get('role', 'staff')
        )
    return make_user


def test_register_user(api_client): #we are sending this data on api and checking the response
    response = api_client.post('/api/users/user/?action=register', {
        "email": "new@example.com",
        "username": "newuser",
        "password": "Testpass123!",
        "role": "staff"
    }, format='json')
    assert response.status_code == 201
    assert response.data['email'] == "new@example.com"
    assert response.data['username']=="newuser"

def test_login_user(api_client, create_user):
    user = create_user()
    response = api_client.post('/api/users/user/?action=login', {
        "email": user.email,
        "password": "Testpass123!"
    }, format='json')
    assert response.status_code == 200
    assert 'access' in response.data

def test_get_profile(api_client, create_user):
    user = create_user()
    response = api_client.post('/api/users/user/?action=login', {
        "email": user.email,
        "password": "Testpass123!"
    }, format='json')
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get('/api/users/user/')
    assert response.status_code == 200
    assert response.data['email'] == user.email

def update_user(api_client, create_user):
    user = create_user()
    response=api_client.put('/api/users/user/?action='),{

    }
def test_update_profile(api_client, create_user):
    # Step 1: Create a user
    user = create_user()

    # Step 2: Login and get token
    response = api_client.post('/api/users/user/?action=login', {
        "email": user.email,
        "password": "Testpass123!"
    }, format='json')
    token = response.data['access']

    # Step 3: Auth with token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Step 4: Send PUT request to update profile
    updated_data = {
        "username": "updateduser",
        "email": "updated@example.com"
    }
    response = api_client.put('/api/users/user/', updated_data, format='json')

    # Step 5: Assertions
    assert response.status_code == 200
    assert response.data['username'] == "updateduser"
    assert response.data['email'] == "updated@example.com"
def test_change_password(api_client, create_user):
    user = create_user()

    # Login to get token
    response = api_client.post('/api/users/user/?action=login', {
        "email": user.email,
        "password": "Testpass123!"
    }, format='json')
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Call change-password endpoint
    data = {
        "old_password": "Testpass123!",
        "new_password": "Newpass456!"
    }
    response = api_client.post('/api/users/user/?action=change-password', data, format='json')

    # Assertions
    assert response.status_code == 200
    assert response.data['detail'] == "Password updated."
def test_list_users_as_admin(api_client, create_user):
    admin_user = create_user(email="admin@example.com", role='administrator')

    # Login as admin
    response = api_client.post('/api/users/user/?action=login', {
        "email": admin_user.email,
        "password": "Testpass123!"
    }, format='json')
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Call list-users
    response = api_client.get('/api/users/user/?action=list-users')

    # Assertions
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert any(user["email"] == "admin@example.com" for user in response.data)