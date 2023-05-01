from django.contrib import admin
from .models import UploadFiles, UploadVideo, UploadImage


class UploadFilesAdmin(admin.ModelAdmin):
    fields = ['author', 'name', 'files']


class UploadImageAdmin(admin.ModelAdmin):
    fields = ['author', 'name', 'logo']


class UploadVideoAdmin(admin.ModelAdmin):
    fields = ['author', 'name', 'video']


admin.site.register(UploadFiles, UploadFilesAdmin)
admin.site.register(UploadImage, UploadImageAdmin)
admin.site.register(UploadVideo, UploadVideoAdmin)

# Register your models here.
