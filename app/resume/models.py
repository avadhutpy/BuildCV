from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Basic(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r"^\+?\d{7,15}$", "Enter a valid phone number.")],
        null=True,
        blank=True,
    )
    short_summary = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    birth_year = models.DateField()
    created = models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    from_year = models.DateField()
    to_year = models.DateField()
    short_description = models.TextField(max_length=250)


class Education(models.Model):
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    from_year = models.DateField()
    to_year = models.DateField()


class Skill(models.Model):
    name = models.CharField(max_length=100)
