from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from pathlib import Path
import fitz

from extract_text.models import UploadDoc
from .serializers import UploadDocModelSerializer

file_path = Path(__file__).resolve().parent.parent.parent


@api_view(["GET"])
def display_extracted_text(request):
    if request.method == "GET":
        latest_data = UploadDoc.objects.last()
        serializer = UploadDocModelSerializer(latest_data)
        pdf_file = fitz.open(
            file_path / serializer.data['pdf_doc'].strip("/")
        )

        for _, page in enumerate(pdf_file.pages(), start=1):
            text = page.get_text()

        # print("\n[display_extracted_text] text: ", text)
        # print("\n[display_extracted_text] pdf_file: ", pdf_file)
        # print("[display_extracted_text] serializer.data['pdf_doc']: ",
        #       serializer.data['pdf_doc'])

        return Response(text)


@api_view(['GET'])
def doc_list_api_view(request):
    if request.method == 'GET':
        qs = UploadDoc.objects.all()
        serializer = UploadDocModelSerializer(qs, many=True)

        return Response(serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_doc_api_view(request):
    if request.method == "POST":
        serializer = UploadDocModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
