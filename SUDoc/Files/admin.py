from django.contrib import admin
from Files.models import File

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ('fileName','createDate', 'uploader')
    search_fields = ('fileName', 'createDate', 'uploader')
    
admin.register(File, FileAdmin)