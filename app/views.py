from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from app.forms import CustomAuthenticationForm, CustomUserCreationForm


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

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()         # important — saves hashed password
            login(request, user)       # optional: log user in immediately
            return redirect('app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'index.html'

def handler405(request, exception=None):
	return render(request, '405.html', status=405)