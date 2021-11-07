from django.urls import path

from .views import doc_list_api_view, upload_doc_api_view, display_extracted_text

urlpatterns = [
    path('documents/', doc_list_api_view, name="documents"),
    path('upload/', upload_doc_api_view, name="upload"),
    path('extracted_text/', display_extracted_text, name="text"),
]
