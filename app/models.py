from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.conf import settings
from coonva import settings
import datetime
import cv2
import os

# Create your models here.

class Class(models.Model):
	name = models.CharField(max_length=25)
	author = models.CharField(max_length=100, default='admin')

	students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="classes", blank=True)
	student_count = models.IntegerField(default=0)