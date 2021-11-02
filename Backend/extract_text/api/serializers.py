from django.db import models
from rest_framework import serializers

from extract_text.models import UploadDoc


class UploadDocModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDoc
        fields = ['id', 'title', 'pdf_doc']
