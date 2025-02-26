from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'role']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Task)