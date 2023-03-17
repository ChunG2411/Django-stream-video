from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='video', null=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])