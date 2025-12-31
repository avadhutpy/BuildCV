from django.test import RequestFactory
from django.test import TestCase, Client
from .factory import BasicModelFactory, ExperienceModelFactory, EducationModelFactory, SkillModelFactory


class BaseFactory(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.client = Client()


class BasicFactory(BaseFactory):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.basics = BasicModelFactory.create_batch(10)
        cls.basic_1 = cls.basics[0]
        
class ExperienceFactory(BaseFactory):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.exps = ExperienceModelFactory.create_batch(10)
        cls.exp_1 = cls.exps[0]
        
class EducationFactory(BaseFactory):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.edus = EducationModelFactory.create_batch(10)
        cls.edu_1 = cls.edus[0]

class SkillFactory(BaseFactory):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.skills = SkillModelFactory.create_batch(10)
        cls.skill_1 = cls.skills[0]
        