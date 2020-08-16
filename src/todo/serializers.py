from rest_framework import serializers
from .models import User, List, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',
                  'created_at', 'updated_at', 'is_deleted')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'title', 'user_id', 'created_at',
                  'updated_at', 'is_deleted')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'is_complete', 'stack_id',
                  'list_id', 'created_at', 'updated_at', 'is_deleted')
