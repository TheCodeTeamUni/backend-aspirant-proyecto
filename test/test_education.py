import json
from unittest import TestCase
from faker import Faker
from application import application as app
from src.models import Education, db


class TestEducation(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):

        educations = Education.query.all()
        for data in educations:
            db.session.delete(data)

        db.session.commit()

    def test_create_education(self):
        new_education = {
            "typeEducation":'Postgrado',
            "level":'Maestria',
            "title": self.data_factory.job(),
            "institution": self.data_factory.company(),            
            "grade": True,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        postEducation = self.client.post(
            "/aspirant/education/1", json=new_education, headers={"Content-Type": "application/json"})

        response = json.loads(postEducation.get_data())

        self.assertEqual(postEducation.status_code, 201)
        self.assertEqual(response['idUser'], 1)

    def test_create_education_with_bad_data(self):
        new_education = {
            "typeEducation":'Postgrado',
            "level":'Maestria',
            "title": self.data_factory.job(),
            "institution": self.data_factory.company(),            
            "grade": "False",
            "startDate": '01-01-2010',
            "endDate": '01-012012'
        }

        postEducation = self.client.post(
            "/aspirant/education/1", json=new_education, headers={"Content-Type": "application/json"})

        self.assertEqual(postEducation.status_code, 400)

    def test_get_education(self):
        new_education = {
            "typeEducation":'Postgrado',
            "level":'Especializacion',
            "title": self.data_factory.job(),
            "institution": self.data_factory.company(),            
            "grade": True,
            "startDate": '01/01/2010',
            "endDate": '01/01/2012'
        }

        postEducation = self.client.post(
            "/aspirant/education/1", json=new_education, headers={"Content-Type": "application/json"})

        getEducation = self.client.get(
            "/aspirant/education/1", headers={"Content-Type": "application/json"})

        response = json.loads(getEducation.get_data())

        self.assertEqual(getEducation.status_code, 200)
        self.assertEqual(len(response), 1)