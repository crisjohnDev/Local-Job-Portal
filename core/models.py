from django.db import models

# Create your models here.
from user.models import User
from django.conf import settings

class JobPost(models.Model):
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_posts"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    job_type = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title