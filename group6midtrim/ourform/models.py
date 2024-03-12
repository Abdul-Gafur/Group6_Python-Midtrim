from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=10)
    subject = models.CharField(max_length=10)
    message = models.TextField(max_length=10)

    def _str_(self):
        return self.name