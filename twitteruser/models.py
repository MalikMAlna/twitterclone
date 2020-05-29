from django.db import models
from django.contrib.auth.models import AbstractUser

# many to many from resources provided in rubric
# Also rewatched the following demo for Custom User with AbstractUser:
# https://s3.us-east-2.amazonaws.com/
# videos.kenzie.academy/
# Software+Engineering+-+Python/2020-05-18--django+custom+users.mp4


class TwitterUser(AbstractUser):
    followers = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.username
