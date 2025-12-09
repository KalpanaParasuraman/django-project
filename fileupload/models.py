from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name