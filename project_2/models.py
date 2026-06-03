from django.db import models
from django.core.validators import MinLengthValidator


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New',
        IN_PROGRESS = 'in_progress', 'In progress',
        COMPLETED = 'completed', 'Completed',
        CLOSED = 'closed', 'Closed',
        PENDING = 'pending', 'Pending',
        BLOCKED = 'blocked', 'Blocked'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        VERY_HIGH = 'very_high', 'Very High'

    title = models.CharField(
        max_length=255,
        unique=True,
        validators=[MinLengthValidator(10)],
    )

    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, default=Status.NEW, choices=Status.choices)    # type: ignore
    priority = models.CharField(max_length=15, choices=Priority.choices)                    # type: ignore

    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
