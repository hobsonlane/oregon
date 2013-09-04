from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=25, null=True)
    url = models.CharField(max_length=128, null=True)
    student_id = models.CharField(max_length=32, null=True)
    teacher = models.BooleanField(default=False)
    parent = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)

class Job(models.Model):
    submitted_by = models.OneToOneField('User', null=True)
    submitted = models.DateTimeField(null=True)
    num_openings = models.IntegerField(default=1, null=True)
    employer_email = models.CharField(max_length=128, null=True)
    employer_name = models.CharField(max_length=128, null=True)
    employer_phone = models.CharField(max_length=25, null=True)
    employer_url = models.CharField(max_length=128, null=True)
    application_instructions = models.TextField(null=True)
    employer_industry = models.CharField(max_length=64)
    description = models.TextField()
    location = models.TextField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=3)
    postal_code = models.CharField(max_length=10)
    compensation = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    hours = models.CharField(max_length=32)
    minimum_age = models.CharField(max_length=32)
    required_experience = models.TextField(null=True)
