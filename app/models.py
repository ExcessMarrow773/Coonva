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
	title = models.CharField(max_length=25)
	teachers = models.ManyToManyField(User,limit_choices_to={'type': 'TEACHER'}, related_name="teaching", blank=True)
	created_on = DateTimeNow

	students = models.ManyToManyField(User,limit_choices_to={'type': 'STUDENT'}, related_name="classes", blank=True)
	assignments = models.ManyToManyField(Assignment, blank=True, null=True, related_name='Class')

	class Meta:
		verbose_name_plural = 'Classes'

	def __str__(self):
		return self.title

class Submission(models.Model):
	created_on = DateTimeNow
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignmentSubmission')
	student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions', limit_choices_to={'type': 'STUDENT'})
