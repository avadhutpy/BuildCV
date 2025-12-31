from django.test import tag
from .test_base import BasicFactory, ExperienceFactory, EducationFactory, SkillFactory

@tag("model", "basic")
class BasicModelTest(BasicFactory):
    def test_basic_count(self):
        self.assertEqual(len(self.basics), 10)

@tag("model", "exp")
class ExperienceModelTest(ExperienceFactory):
    def test_basic_count(self):
        self.assertEqual(len(self.exps), 10)

@tag("model", "edu")
class EducationModelTest(EducationFactory):
    def test_basic_count(self):
        self.assertEqual(len(self.edus), 10)

@tag("model", "skill")
class SkillModelTest(SkillFactory):
    def test_basic_count(self):
        self.assertEqual(len(self.skills), 10)
