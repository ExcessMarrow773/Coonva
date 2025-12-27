from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from coonva import settings
import datetime
import cv2
import os

User = get_user_model()

DateTimeNow = models.DateTimeField(default=timezone.now)

# Create your models here.


class Assignment(models.Model):
	name = models.CharField(max_length=255)
	due_at = models.DateTimeField()
	created_on = DateTimeNow
	locks_at = models.DateTimeField()

	details = models.TextField()

	def __str__(self):
		return self.name


class Class(models.Model):
	name = models.CharField(max_length=25)
	author = models.CharField(max_length=100, default='admin')

	students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="classes", blank=True)
	student_count = models.IntegerField(default=0)