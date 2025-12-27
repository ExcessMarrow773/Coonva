from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {
			'fields': ('username', 'password')
		}),
		('Personal info', {
			'fields': ('first_name', 'last_name', 'email', 'profile_image')
		}),
		('Permissions', {
			'fields': (
				'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
			)
		}),
		('Important dates', {
			'fields': ('last_login', 'date_joined')
		}),
		(None, {
			'fields': ['type']
		})
	)

admin.site.register(CustomUser, CustomUserAdmin)