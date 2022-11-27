from .models import TodoList
from rest_framework import serializers


class TodoListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = TodoList
        fields = ("id", "title", "done", "author_ip", "create_date", "done_date")
