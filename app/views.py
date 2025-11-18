from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


from itertools import chain
from operator import attrgetter
import os
import json

User = get_user_model()
# Create your views here.

def index(request):
	context = {
	}
	return render(request, 'app/index.html', context)

