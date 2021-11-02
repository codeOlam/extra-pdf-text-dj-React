from django.urls import path

from .views import doc_list_api_view

urlpatterns = [
    path('documents/', doc_list_api_view, name="documents"),
]
