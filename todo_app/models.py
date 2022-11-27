from django.db import models


class TodoList(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    done = models.BooleanField()
    author_ip = models.CharField(max_length=15)
    create_date = models.DateTimeField()
    done_date = models.DateTimeField()
