from django.db import models

class HomeImage(models.Model):
    title = models.CharField(max_length=255,default="")
    img = models.FileField(upload_to='home/')
    order = models.IntegerField(default=0)

