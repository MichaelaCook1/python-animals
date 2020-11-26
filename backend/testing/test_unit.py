from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = ["Lion", "Dog", "Cat", "Cow", "Pig", "Snake"]
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
                url_for('noise'),
                data='Lion',
                follow_redirect=True
                )
        self.assertIn(b'ROAR', response.data)

    def test_noise_dog(self):
        response = self.client.post(
                url_for('noise'),
                data='Dog',
                follow_redirect=True
                )
        self.assertIn(b'WOOF', response.data)
