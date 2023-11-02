import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import PersonalInformation, db


class TestPersonalInformation(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.name = self.data_factory.name()
        self.lastName = self.data_factory.last_name()
        self.typeDocument = self.data_factory.random_element(
            elements=('CC', 'TI', 'CE'))
        self.document = self.data_factory.ssn()
        self.gender = self.data_factory.random_element(
            elements=('M', 'F', 'O'))
        self.alternativeEmail = self.data_factory.email()
        self.telephone = self.data_factory.phone_number()
        self.country = self.data_factory.country()
        self.address = self.data_factory.address()
        self.birthdate = '01/01/1990'
        self.description = self.data_factory.text()
        self.photo = self.data_factory.image_url()

        new_personal = {
            "name": self.name,
            "lastName": self.lastName,
            "typeDocument": self.typeDocument,
            "document": self.document,
            "gender": self.gender,
            "alterntiveEmail": self.alternativeEmail,
            "telephone": self.telephone,
            "country": self.country,
            "address": self.address,
            "birthdate": self.birthdate,
            "description": self.description,
            "photo": self.photo}

        self.client.post(
            "/aspirant/personal/1", json=new_personal, headers={"Content-Type": "application/json"})

    def tearDown(self):

        personales = PersonalInformation.query.all()
        for data in personales:
            db.session.delete(data)

        db.session.commit()

    def test_create_personal_information(self):

        new_personal = {
            "name": self.data_factory.name(),
            "lastName": self.data_factory.last_name(),
            "typeDocument": self.data_factory.random_element(elements=('CC', 'TI', 'CE')),
            "document": self.data_factory.ssn(),
            "gender": self.data_factory.random_element(elements=('M', 'F', 'O')),
            "alterntiveEmail": self.data_factory.email(),
            "telephone": self.data_factory.phone_number(),
            "country": self.data_factory.country(),
            "address": self.data_factory.address(),
            "birthdate": '13/05/1992',
            "description": self.data_factory.text(),
            "photo": self.data_factory.image_url()
        }

        postPersonal = self.client.post(
            "/aspirant/personal/2", json=new_personal, headers={"Content-Type": "application/json"})

        response = json.loads(postPersonal.get_data())

        self.assertEqual(response["id"], 2)
        self.assertEqual(postPersonal.status_code, 201)

    def test_create_personal_information_fail(self):

        new_personal = {
            "idUser": 2,
            "birthdate": '13-05-1992',
            "description": self.data_factory.text(),
            "photo": self.data_factory.image_url()}

        postPersonal = self.client.post(
            "/aspirant/personal/2", json=new_personal, headers={"Content-Type": "application/json"})

        self.assertEqual(postPersonal.status_code, 400)

    def test_get_personal_information(self):

        getPersonal = self.client.get("/aspirant/personal/1")

        response = json.loads(getPersonal.get_data())

        self.assertEqual(getPersonal.status_code, 200)
        self.assertEqual(response["name"], self.name)

    def test_ping_aspirant(self):

        endpoint_ping = "/"
        headers = {'Content-Type': 'application/json'}

        sol_ping = self.client.get(endpoint_ping,
                                   headers=headers)

        self.assertEqual(sol_ping.status_code, 200)

    def test_fail_page(self):

        endpoint_usuario = "/aspirant/fail"
        headers = {'Content-Type': 'application/json'}

        sol_logUser = self.client.get(endpoint_usuario,
                                      headers=headers)

        self.assertEqual(sol_logUser.status_code, 404)
