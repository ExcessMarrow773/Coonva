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

class CustomUser(AbstractUser):
	profile_image = models.ImageField(upload_to='pfps/', default='static/img/pfp.png')

	# make email unique because it's used as the USERNAME_FIELD
	email = models.EmailField(max_length=254, unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']