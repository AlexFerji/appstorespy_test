from rest_framework import viewsets

from .models import UploadFiles, UploadImage, UploadVideo
from .serializers import FilesListSerializer, FilesCreateSerializer,\
    ImageListSerializer, ImageCreateSerializer,\
    VideoListSerializer, VideoCreateSerializer


class UploadFilesView(viewsets.ModelViewSet):
    queryset = UploadFiles.objects.all()
    serializer_class = FilesListSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return FilesCreateSerializer

        return FilesListSerializer


class UploadImageView(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = ImageListSerializer


    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ImageCreateSerializer

        return ImageListSerializer


class UploadVideoView(viewsets.ModelViewSet):
    queryset = UploadVideo.objects.all()
    serializer_class = VideoListSerializer


    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return VideoCreateSerializer

        return VideoListSerializer




