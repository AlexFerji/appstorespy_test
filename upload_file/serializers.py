from rest_framework import serializers
from moviepy.editor import *
from .models import UploadFiles, UploadImage, UploadVideo


class FilesListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = UploadFiles
        fields = ('__all__')


class FilesCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    info = serializers.CharField(read_only=True)

    class Meta:
        model = UploadFiles
        fields = ('__all__')

    def create(self, validated_data,  *args, **kwargs):
        instance = UploadFiles.objects.create(**validated_data)
        instance.info = "{0} {1}".format("Колличество строк:", len(instance.files.readlines()))
        instance.save()

        return (instance)





class ImageListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = UploadImage
        fields = ("__all__")


class ImageCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    info = serializers.CharField(read_only=True)

    class Meta:
        model = UploadImage
        fields = ("__all__")

    def create(self, validated_data, *args, **kwargs):
        instance = UploadImage.objects.create(**validated_data)
        instance.info = "{0} {1} {2} {3} {4}".format\
                                    ("Размер изменён с:",instance.logo.height, "*",  instance.logo.width, "до 200px")
        instance.save()

        return (instance)


class VideoListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = UploadVideo
        fields = ("__all__")


class VideoCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UploadVideo
        fields = ("__all__")

    def create(self, validated_data, *args, **kwargs):
        instance = UploadVideo.objects.create(**validated_data)
        clip1 = instance.video.path
        clip2 = VideoFileClip(clip1)
        clip2 = clip2.subclip(0, 10)
        clip2.write_videofile(clip1, fps=30, codec="libx264")
        instance.save()

        return (instance)