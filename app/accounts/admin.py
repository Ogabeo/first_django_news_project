from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'full_name', 'last_login','is_staff' )
    list_display_links=('id', 'username')

admin.site.register(User, UserAdmin)

