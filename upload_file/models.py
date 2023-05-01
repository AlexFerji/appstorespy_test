from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from datetime import datetime

from .helpers import resize_logo


def user_video(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.author.username + "-" + date_time + filename
    return 'profile/video/{0}/{1}'.format(instance.author.username, saved_file_name, filename)


def user_image(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.author.username + "-" + date_time + filename
    return 'profile/image/{0}/{1}'.format(instance.author.username, saved_file_name, filename)


def user_files(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.author.username + "-" + date_time + filename
    return 'profile/files/{0}/{1}'.format(instance.author.username, saved_file_name, filename)


class UploadFiles(models.Model):
    author = models.ForeignKey(to=User, null=True, related_name='post', on_delete=models.SET_NULL)
    name = models.CharField(max_length=25)
    files = models.FileField(upload_to=user_files,
                             null=True,
                             validators=[validators.FileExtensionValidator(['txt', 'pdf'],
                                                                           message='fiels должен быть формата txt или pdf')])
    info = models.CharField(max_length=500, null=True)


    def __str__(self):
        return f'{self.name} by {self.author.username}'


class UploadImage(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to=user_image, null=True, height_field=None, width_field=None)
    info = models.CharField(max_length=300)


    def __str__(self):
        return f'{self.name} by {self.author.username}'


    def save(self, *args, **kwargs):
        super(UploadImage, self).save(*args, **kwargs)

        if self.logo:
            resize_logo(self)


class UploadVideo(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=25)
    video = models.FileField(upload_to=user_video, null=True)


    def __str__(self):
        return f'{self.name} by {self.author.username}'



