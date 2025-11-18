from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.register, name='register'),
]