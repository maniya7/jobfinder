
import uuid
from django.db import models
from django.conf import settings


class Company(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(
        upload_to='company_logos/',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class Employer(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employer'
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employers'
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)

    def str(self):
        return f'{self.first_name} {self.last_name}'
