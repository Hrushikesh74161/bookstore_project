from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'email', 'is_staff']