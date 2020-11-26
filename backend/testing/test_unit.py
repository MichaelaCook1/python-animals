from flask import url_for
from flask_testing import TestCase

from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b"Lion",b"Dog", b"Cat", b"Cow", b"Pig", b"Snake"]
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


    def test_noise_cat(self):
        response = self.client.post(
                url_for('noise'),
                data='Cat',
                follow_redirect=True
                )
        self.assertIn(b'MEOW', response.data)


    def test_noise_cow(self):
        response = self.client.post(
                url_for('noise'),
                data='Cow',
                follow_redirect=True
                )
        self.assertIn(b'MOO', response.data)


    def test_noise_pig(self):
        response = self.client.post(
                url_for('noise'),
                data='Pig',
                follow_redirect=True
                )
        self.assertIn(b'OINK', response.data)


    def test_noise_snake(self):
        response = self.client.post(
                url_for('noise'),
                data='Snake',
                follow_redirect=True
                )
        self.assertIn(b'HISS', response.data)
