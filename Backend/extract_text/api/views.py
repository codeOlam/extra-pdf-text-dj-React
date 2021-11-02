from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from extract_text.models import UploadDoc
from .serializers import UploadDocModelSerializer

# class UploadDocApiView(APIView):
#     http_method_names = ['GET', 'POST']


@api_view(['GET', 'POST'])
def doc_list_api_view(request):
    if request.method == 'GET':
        qs = UploadDoc.objects.all()
        serializer = UploadDocModelSerializer(qs, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UploadDocModelSerializer(data=request.data)

        if serializer.is_valid():
            # logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
