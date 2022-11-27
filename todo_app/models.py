from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models


id (int, identyfikator), title (str, tytuł
zadania), done (bool, czy zadanie zostało zrobione), author_ip (str, adres ip osoby
tworzącej), created_date (datetime, data utworzenia), done_date (datetime, data
zakończenia zadania