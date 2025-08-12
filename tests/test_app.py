import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_main_route_returns_welcome():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert response.data == b'Welcome!'

def test_hello_route_returns_response():
    tester = app.test_client()
    response = tester.get('/how%20are%20you')
    assert response.status_code == 200
    assert response.data == b'I am good, how about you?'

def test_missing_route_returns_404():
    tester = app.test_client()
    response = tester.get('/missing')
    assert response.status_code == 404
