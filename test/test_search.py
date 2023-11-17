from unittest import TestCase
from faker import Faker
from application import application as app


class TestPersonalInformation(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def test_get_aspirants_skill(self):
        response = self.client.get(
            "/aspirant/Python", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_get_aspirant(self):
        response = self.client.get(
            "/aspirant/1", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_get_aspirants(self):
        response = self.client.get(
            "/aspirant", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)