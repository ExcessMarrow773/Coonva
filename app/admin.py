from django.contrib import admin
from app.models import Class, Assignment, Submission

# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
	list_display = ('title', 'student_count')
	list_filter = ('created_on', )
	date_hierarchy = 'created_on'
	search_fields = ('title', 'teachers')

	def student_count(self, obj):
		return obj.students.count()
	student_count.short_description = 'Student Count'

	fieldsets = [
		(None, {
			'fields': ('title', 'teachers', 'students', 'assignments')
			}
		)
	]

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_on', 'due_at', 'locks_at')
	list_filter = ('due_at', 'locks_at', 'created_on')
	date_hierarchy = 'due_at'
	search_fields =['name']

	def assignment_class(self, obj):
		return obj.entry_set.all()

	fieldsets = [
		(None, {
			'fields': ('name', 'details', 'type')
			}
		),
		('Dates', {
			'fields': ('due_at', 'created_on', 'locks_at')
			}
		),
		('Student Data', {
			'fields': ['submitted']
			}
		)
		]

	readonly_fields = ('submitted', 'created_on')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
	readonly_fields = ('student', 'created_on', 'URL', 'file', 'text', 'assignment')
	list_display = ('student', 'created_on')
	list_filter = ['created_on']
	date_hierarchy = 'created_on'
	search_fields = ['student']