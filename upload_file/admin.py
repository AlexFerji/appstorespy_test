from django.contrib import admin
from .models import UploadFiles


class UploadAdmin(admin.ModelAdmin):
    fields = ['author', 'name', 'files', 'logo', 'video']



admin.site.register(UploadFiles, UploadAdmin)

# Register your models here.
