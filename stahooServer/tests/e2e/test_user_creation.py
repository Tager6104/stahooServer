from django.contrib.auth.hashers import make_password


def test_user_can_be_created_with_provided_credentials(client, django_user_model):

    post_data = {
        'username': 'test_user',
        'password': 'test_password',
        'email': 'test_email@test.com',
        'first_name': 'Test',
        'last_name': 'User'
    }

    response = client.post('/api/stahoo/create_user/', post_data)
    assert response.status_code == 201

    users = django_user_model.objects.all()
    assert len(users) == 1

    assert users[0].username == post_data['username']
    assert users[0].password == response.data['password']
    assert users[0].email == post_data['email']
    assert users[0].first_name == post_data['first_name']
    assert users[0].last_name == post_data['last_name']
