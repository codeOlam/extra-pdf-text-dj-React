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
        try:
            pdf_file = fitz.open(
                file_path / serializer.data['pdf_doc'].strip("/")
            )

            for _, page in enumerate(pdf_file.pages(), start=1):
                text = page.get_text()

            return Response(text)
        except:
            # this is just a rough way of catching this error.
            # in the future i will be validating to make sure only pdf can be uploaded from frontend
            return Response("Make sure the file uploaded is in pdf formatt!")


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
