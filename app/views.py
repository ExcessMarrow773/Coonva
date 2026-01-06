from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from itertools import chain
from operator import attrgetter
from .models import Class, Assignment, Submission

import os
import json


User = get_user_model()
# Create your views here.

def index(request):
	context = {
	}
	return render(request, 'app/index.html', context)

def classList(request):
	classes = Class.objects.filter(students=request.user.id)
	context = {
		'classes': classes
	}
	return render(request, 'app/classList.html', context)

def classView(request, pk):
	classView = Class.objects.get(pk=pk)
	assignments = classView.assignments.all()
	context = {
		'class': classView,
		'assignments': assignments
	}
	return render(request, 'app/class.html', context)

def assignmentView(request, pk):
	assignment = Assignment.objects.get(pk=pk)

	if request.method == "POST":
		form = SubmissionForm(request.POST, request.FILES)

		if request.user in assignment.submitted.all():
			return redirect('app:assignments')
		if form.is_valid():
			if form.cleaned_data["URL"]:
				URL=form.cleaned_data["URL"]
			else: URL = None

			if form.cleaned_data["text"]:
				text=form.cleaned_data["text"]
			else: text = None

			if form.cleaned_data["file"]:
				file=form.cleaned_data["file"]
			else: file = None
			submission = Submission(
				student=request.user,
				assignment=assignment,
				URL=URL,
				text=text,
				file=file,
			)
			submission.save()
			assignment.submitted.add(request.user)
			assignment.save()
			return redirect('app:index')
	else:
		form = SubmissionForm()
	print(form)

	context = {
		'assignment': assignment,
		'form': form
	}
	return render(request, 'app/assignment.html', context)