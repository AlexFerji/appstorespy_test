from rest_framework import serializers
# from moviepy.editor import *
# import moviepy.editor as mp
from moviepy.editor import VideoFileClip

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
        instance.info = len(instance.files.readlines())
        instance.save()

        clip1 = instance.video.path
        clip = VideoFileClip(clip1)
        clip = clip.subclip(0, 10)
        clip.write_videofile(clip1)
        clip.close()
        instance.video = clip
        instance.save()


        return (instance)



