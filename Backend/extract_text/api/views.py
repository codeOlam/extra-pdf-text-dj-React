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
print("file_path", file_path)
pdf_file = fitz.open(
    file_path / 'docs/The_Purpose_and_Power_of_Love__Marriage__PDFDrive_.pdf')

print("pdf_file: ", pdf_file)


# @api_view(["GET"])
# def display_extracted_text(request):
#     if request.method == "GET":
#         queryset = UploadDoc.objects.filter()


@api_view(['GET'])
def doc_list_api_view(request):
    if request.method == 'GET':
        qs = UploadDoc.objects.all()
        serializer = UploadDocModelSerializer(qs, many=True)
        print("\n[serializer.pdf_doc]: ", serializer.data[1])

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
