from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False, unique=True)
    done = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    