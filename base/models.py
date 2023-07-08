from django.db import models

# Create your models here.
class ChatInput(models.Model):
    role_choices = [
        ('system', 'System'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=10, choices=role_choices)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.role}: {self.content}'
