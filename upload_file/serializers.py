from rest_framework import serializers
from moviepy.editor import *

from .models import UploadFiles


class UploadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = UploadFiles
        fields = ('__all__')



class CreateUploadSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    info = serializers.CharField(read_only=True)
    class Meta:
        model = UploadFiles
        fields = ('__all__')

    def create(self, validated_data,  *args, **kwargs):

        instance = UploadFiles.objects.create(**validated_data)

        if instance.files:
            instance.info = "{0} {1}".format("Колличество строк:", len(instance.files.readlines()))
        elif instance.logo:
            instance.info = "{0} {1} {2} {3} {4}".format\
                                ("Размер изменён с:",instance.logo.height, "*",  instance.logo.width, "до 200px"),
            instance.save()
        elif instance.video:
            clip1 = instance.video.path
            clip2 = VideoFileClip(clip1)
            clip2 = clip2.subclip(0, 10)
            clip2.write_videofile(clip1, fps=30, codec="libx264")
        instance.save()

        return (instance)



