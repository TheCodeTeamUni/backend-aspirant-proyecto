import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from application import application as app
from src.models import Skill, db


class Testkill(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def tearDown(self):

        skills = Skill.query.all()
        for data in skills:
            db.session.delete(data)

        db.session.commit()

    def test_create_skill(self):
        new_skill = {
            "skill": self.data_factory.job(),
            "level": random.randint(0, 100),
            "experience": self.data_factory.text()
        }

        postSkill = self.client.post(
            "/aspirant/skill/1", json=new_skill, headers={"Content-Type": "application/json"})

        response = json.loads(postSkill.get_data())

        self.assertEqual(postSkill.status_code, 201)
        self.assertEqual(response['idUser'], 1)

    def test_create_skill_with_bad_data(self):
        new_skill = {
            "skill": self.data_factory.job(),
            "level": self.data_factory.text(),
            "experience": self.data_factory.text()
        }

        postSkill = self.client.post(
            "/aspirant/skill/1", json=new_skill, headers={"Content-Type": "application/json"})

        self.assertEqual(postSkill.status_code, 400)

    def test_get_skills(self):
        skill1 = Skill(idUser=1, skill=self.data_factory.job(),
                       level=random.randint(0, 100), experience=self.data_factory.text())
        skill2 = Skill(idUser=1, skill=self.data_factory.job(),
                       level=random.randint(0, 100), experience=self.data_factory.text())

        db.session.add(skill1)
        db.session.add(skill2)
        db.session.commit()

        getSkills = self.client.get("/aspirant/skill/1")

        response = json.loads(getSkills.get_data())

        self.assertEqual(getSkills.status_code, 200)
        self.assertEqual(len(response), 2)
