from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from .choices import GENDERS

class Project(models.Model):
    uuid = models.CharField(max_length=40, unique=True, default=None)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True, blank=True)
    json_data = JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    month = models.IntegerField(null=False, default=1)
    year = models.IntegerField(null=False, default=2019)
    gender = models.CharField(max_length=10, choices=GENDERS)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()