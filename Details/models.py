from django.db import models

# Create your models here.

class ExtractedData(models.Model):
    site = models.CharField(max_length=255)
    xpath = models.CharField(max_length=255)
    data = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

