from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    pass

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        get_latest_by = 'updated_at'
        ordering = ['updated_at']


class List(models.Model):
    title = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table: 'lists'
        get_latest_by = 'updated_at'
        ordering = ['updated_at']


class Task(models.Model):
    description: models.CharField(max_length=200)
    is_complete: models.BooleanField(default=False)
    stack_id: models.IntegerField()
    list_id: models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        db_table: 'tasks'
        get_latest_by = 'updated_at'
        ordering = ['updated_at']
