import factory
from resume.models import Basic, Experience, Education, Skill


class BasicModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Basic
    # https://factoryboy.readthedocs.io/en/stable/reference.html#factory.Factory.generate
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    birth_year = factory.Faker("date_of_birth")
    short_summary = factory.Faker("text", max_nb_chars=150)
    image = factory.django.ImageField(color="blue")


class ExperienceModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Experience

    company_name = factory.Faker("company")
    role = factory.Faker("job")
    from_year = factory.Faker("past_date", start_date="-2y")
    to_year = factory.Faker("date")
    short_description = factory.Faker("text", max_nb_chars=250)

class EducationModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Education
    university = factory.Faker("pystr", max_chars=15)
    degree = factory.Faker("pystr", max_chars=15)
    from_year = factory.Faker("past_date", start_date="-3y")
    to_year = factory.Faker("date")

class SkillModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill
    name = factory.Faker("word")