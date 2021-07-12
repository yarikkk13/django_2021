from django.contrib import admin

from .models import UserModel


# Register your models here.
# admin.site.register(UserModel)
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'userName', 'age', 'email')
