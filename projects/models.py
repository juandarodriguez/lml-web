from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import JSONField

class Project(models.Model):
    uuid = models.CharField(max_length=40, unique=True, default=None)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    json_data = JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


