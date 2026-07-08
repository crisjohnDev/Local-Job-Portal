from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employeer', 'Employeer'),
        ('appplicant', 'Applicant')
    )

    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='applicant')
    company = models.CharField(max_length=200, null=True, blank=True)
    company_profile = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.username