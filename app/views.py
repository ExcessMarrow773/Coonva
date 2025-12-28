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

	context = {
		'assignment': assignment,
	}
	return render(request, 'app/assignment.html', context)