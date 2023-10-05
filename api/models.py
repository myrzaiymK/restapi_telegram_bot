from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)

class Message(models.Model):
    date_sent = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class TelegramBotToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=100)

