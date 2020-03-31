from django.db import models

# Create your models here.

class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(default='')


class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default='')