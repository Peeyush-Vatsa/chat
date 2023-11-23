from django.db import models

# Create your models here.
    
class Message(models.Model):
    name = models.CharField(max_length=64, default='Anonymous')
    message = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message