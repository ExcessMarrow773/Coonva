from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('classes', views.classList, name='classes'),
    path('class/<pk>', views.classView, name='classView'),
]