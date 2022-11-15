from django.db import models

from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
