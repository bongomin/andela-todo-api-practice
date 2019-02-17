import pytest
import json
from app.users.users import Users
from app.views import app


userInstance = Users()


# @pytest.fixture
# def client(request):
#     test_client = app.test_client()
#     return test_client


def test_signup():
    data = {"username": "Okello", "password": "Nyeko"}
    test_client = app.test_client()
    response = test_client.post('/signup', json=data)
    assert response.status_code == 201
