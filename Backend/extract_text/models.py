from django.db import models

# Create your models here.


class UploadDoc(models.Model):
    title = models.CharField(max_length=254)
    pdf_doc = models.FileField(upload_to='docs', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
