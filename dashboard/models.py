from django.db import models

# Create your models here.
class Email(models.Model):
    message_id = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject