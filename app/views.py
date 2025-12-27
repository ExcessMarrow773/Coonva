from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from itertools import chain
from operator import attrgetter
from .models import Class

import os
import json


User = get_user_model()
# Create your views here.

def index(request):
	context = {
	}
	return render(request, 'app/index.html', context)

