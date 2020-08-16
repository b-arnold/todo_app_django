from django.contrib import admin, auth
from django.contrib.auth import get_user_model

from .forms import UserChangeForm, UserCreationForm
from .models import User, List, Task


class UserAdmin(auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username']


admin.site.register(User, UserAdmin)
admin.site.register(List)
admin.site.register(Task)

# Register your models here.
