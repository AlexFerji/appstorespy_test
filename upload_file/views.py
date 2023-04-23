from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import UploadFiles
from .serializers import UploadSerializer, CreateUploadSerializer


class UploadView(viewsets.ModelViewSet):
    queryset = UploadFiles.objects.all()
    serializer_class = UploadSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return CreateUploadSerializer

        return UploadSerializer





