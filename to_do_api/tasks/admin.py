from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'done','due_date')
    list_filter = ('done','due_date')
    search_fields = ('title', 'description','due_date')
