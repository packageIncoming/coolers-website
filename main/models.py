from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(default="Title",max_length=256)

    def __str__(self):
        return self.title