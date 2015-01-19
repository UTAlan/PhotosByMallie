from django.db import models

class Investment(models.Model):
    title = models.CharField(max_length=255,default='')
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "Investment"

