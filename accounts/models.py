from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.conf import settings
from coonva import settings
import datetime
import cv2
import os
# Create your models here.

TYPE_CHOICES = {
	'ADMIN': 'Administrator',
	'TEACHER': 'Teacher',
	'STUDENT': 'Student',
}

class CustomUser(AbstractUser):
	profile_image = models.ImageField(upload_to='pfps/', default='static/img/pfp.png')

	# make email unique because it's used as the USERNAME_FIELD
	email = models.EmailField(max_length=254, unique=True)
	type = models.CharField(choices=TYPE_CHOICES, max_length=16, default='ADMIN')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']