from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	profile_image = models.ImageField(upload_to='pfps/', default='static/img/pfp.png')


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']