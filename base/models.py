from django.db import models

# Create your models here.
class Comments(models.Model):
    text = models.TextField()
    email = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)

