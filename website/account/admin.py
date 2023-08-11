# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Profile

class UserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = User
    list_display = ("id", "last_name", "first_name", "email", "role")
    ordering = ("last_name", "first_name",)
    fieldsets = (
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'role')
        }),
        ('Password', {
            'fields': ('password',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(User, UserAdmin)

@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'state')
