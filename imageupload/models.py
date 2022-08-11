from django.db import models
from django.db.models import CharField

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=50)
    images_Main_Img = models.ImageField(upload_to='images/')
    # objects = models.Manager()