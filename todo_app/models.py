from django.db import models


class TodoList(models.Model):
    id = models.IntegerField()
    title = models.CharField()
    done = models.BooleanField()
    author_ip = models.CharField()
    create_date = models.DateTimeField()
    done_date = models.DateTimeField()
