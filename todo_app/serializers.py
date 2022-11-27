from .models import TodoList
from rest_framework import serializers


class TodoListSerializer(serializers.ModelSerializer):

    list = serializers.HyperlinkedRelatedField
    read_only = True
    view_name = "todolist"

    class Meta:

        model = TodoList
        fields = ("id", "title", "done", "author_ip", "create_date", "done_date")
