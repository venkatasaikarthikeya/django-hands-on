from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    todo_summary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'status',
            'todo_summary'
        ]

    def get_todo_summary(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Todo):
            return None
        return obj.get_summary()