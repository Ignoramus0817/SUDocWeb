from django.contrib import admin
from Users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'email_Address')
    search_fields = ('userName',)

admin.site.register(User, UserAdmin)