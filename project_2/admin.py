from django.contrib import admin

from .models import Project, Task, Tag, ProjectFile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
    ]
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'project',
        'status',
        'priority',
        'created_at',
        'due_date',
        'assignee'
    ]
    search_fields = ['title']
    list_filter = [
        'status',
        'priority',
        'project',
        'created_at',
        'due_date'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'file',
        'created_at'
    ]