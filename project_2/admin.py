from django.contrib import admin

from .models import Project, Task, Tag, ProjectFile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_count_of_files', 'created_at',]
    search_fields = ['name']

    def display_count_of_files(self, obj):
        return obj.count_of_files

    display_count_of_files.short_description = 'Count of Files'


    def replace_spaces_with_underscores(self, request, objects):
        for obj in objects:
            obj.name = obj.name.replace(' ', '_')
            obj.save()
        return objects

    replace_spaces_with_underscores.short_description = 'Replace spaces with underscores'
    actions = ['replace_spaces_with_underscores']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'created_at', 'due_date', 'assignee']
    search_fields = ['title']
    list_filter = ['status', 'priority', 'project', 'created_at', 'due_date']

    def change_tasks_status_on_completed(self, request, objects):
        for obj in objects:
            obj.status = 'completed'
            obj.save()
        return objects

    change_tasks_status_on_completed.short_description = 'Change status on Completed'
    actions = ['change_tasks_status_on_completed']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

