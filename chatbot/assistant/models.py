from django.db import models

# Create your models here.

class OpenAIMessage(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
