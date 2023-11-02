import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import WorkExperience, db


class TestPersonalInformation(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):

        personales = WorkExperience.query.all()
        for data in personales:
            db.session.delete(data)

        db.session.commit()

    def test_create_work_experience(self):
        new_work = {
            "company": self.data_factory.company(),
            "position": self.data_factory.job(),
            "actualJob": False,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        postWork = self.client.post(
            "/aspirant/work/1", json=new_work, headers={"Content-Type": "application/json"})

        response = json.loads(postWork.get_data())

        self.assertEqual(postWork.status_code, 201)
        self.assertEqual(response['idUser'], 1)

    def test_create_work_experience_with_bad_data(self):
        new_work = {
            "company": self.data_factory.company(),
            "position": self.data_factory.job(),
            "actualJob": False,
            "startDate": '01-01-2010',
            "endDate": '01-01-2012'
        }

        postWork = self.client.post(
            "/aspirant/work/1", json=new_work, headers={"Content-Type": "application/json"})

        self.assertEqual(postWork.status_code, 400)

    def test_get_work_experience(self):
        new_work = {
            "company": 'Company Test',
            "position": self.data_factory.job(),
            "actualJob": False,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        self.client.post(
            "/aspirant/work/1", json=new_work, headers={"Content-Type": "application/json"})

        getWork = self.client.get(
            "/aspirant/work/1", headers={"Content-Type": "application/json"})

        response = json.loads(getWork.get_data())

        self.assertEqual(getWork.status_code, 200)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['company'], 'Company Test')
