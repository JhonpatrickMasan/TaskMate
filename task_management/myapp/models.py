# myapp/models.py

from django.db import models

# Define the Kanban columns (To Do, In Progress, Done)
KANBAN_COLUMNS = [
    ('TODO', 'To Do'),
    ('IN_PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=KANBAN_COLUMNS,
        default='TODO',
    )
    due_date = models.DateField(blank=True, null=True)  # New field
    tags = models.CharField(max_length=200, blank=True, null=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
