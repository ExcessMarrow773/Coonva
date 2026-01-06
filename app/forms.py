from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.utils import timezone
from app.models import Assignment, Submission
from django.contrib.auth import get_user_model

User = get_user_model()

class SubmissionForm(forms.ModelForm):
	class Meta:
		model = Submission
		fields = ['URL', 'file', 'text']